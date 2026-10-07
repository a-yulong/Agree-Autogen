"""Recompute manuscript statistics from measured fields and raw rubric ratings.

Uses only the standard library. No plotting, provider calls, or manuscript values.
"""
from pathlib import Path
from collections import Counter
from statistics import mean
import ast,csv,hashlib,json,math,os

ROOT=Path(__file__).resolve().parents[1]
MODEL_NAMES={'full':'Qwen3-Coder-30B','gpt':'GPT-5.4','codestral':'Codestral-2508',
             'llama':'Llama-3.1-70B','gemma':'Gemma-3-27B'}

def aggregate(rows):
    n=len(rows);first=sum(r['success'] and r['repair_count']==0 for r in rows)
    final=sum(r['success'] for r in rows)
    recovered=sum(r['success'] and r['repair_count'] is not None and r['repair_count']>0 for r in rows)
    assert first+recovered==final
    initial=n-first
    runtime=sum(r['runtime'] for r in rows);tokens=sum(r['token_stats']['total_tokens'] for r in rows)
    rounds=lambda good:dict(sorted(Counter(str(r['repair_count']) for r in rows if r['success']==good and r['repair_count'] is not None).items()))
    return {'n':n,'first':first,'final':final,'recovered':recovered,'initial_failures':initial,
            'first_pct':100*first/n,'final_pct':100*final/n,'recovery_pct':100*recovered/initial if initial else None,
            'gain_pp':100*(final-first)/n,'dependence_pct':100*recovered/final if final else None,
            'runtime':runtime/n,'tokens':tokens/n,'runtime_per_valid':runtime/final if final else None,
            'tokens_per_valid':tokens/final if final else None,'success_rounds':rounds(True),'failure_rounds':rounds(False),
            'missing_rounds':sum(r['repair_count'] is None for r in rows),'stage_errors':sum(bool(r['stage_error']) for r in rows)}

def truth(value):
    assert str(value).lower() in ('true','false'),value
    return str(value).lower()=='true'

def icc(pairs):
    n=len(pairs);k=2;rowmeans=[mean(r) for r in pairs]
    colmeans=[mean(r[j] for r in pairs) for j in range(k)];grand=mean(rowmeans)
    msr=k*sum((r-grand)**2 for r in rowmeans)/(n-1)
    msc=n*sum((c-grand)**2 for c in colmeans)/(k-1)
    mse=sum((pairs[i][j]-rowmeans[i]-colmeans[j]+grand)**2 for i in range(n) for j in range(k))/((n-1)*(k-1))
    denom=msr+(k-1)*mse+k*(msc-mse)/n
    return (msr-mse)/denom if denom else None

def assess(rows,run,weights):
    dims=list(weights);wi=[round(weights[d]*100) for d in dims]
    assert sum(wi)==100 and all(math.isclose(weights[d]*100,w) for d,w in zip(dims,wi))
    records=[];seen=set()
    for row in rows:
        cid=f"Case{int(row['case_id'][4:]):03d}"
        assert cid in run and cid not in seen,cid
        seen.add(cid)
        scores=[]
        for prefix in ('expert_1','expert_2'):
            assert row[prefix+'_status']=='ok',(cid,prefix,row[prefix+'_status'])
            dimscores=[float(row[f'{prefix}_{d}']) for d in dims]
            assert all(x.is_integer() and 1<=x<=5 for x in dimscores)
            scores.append([int(x) for x in dimscores])
        a,b=scores;sa=sum(x*w for x,w in zip(a,wi));sb=sum(x*w for x,w in zip(b,wi))
        averages=[(x+y)/2 for x,y in zip(a,b)];combined=(sa+sb)/200
        strict=sa+sb>=800 and min(averages)>=3
        valid=run[cid]['success'];assert truth(row['validator_pass'])==valid
        assert math.isclose(float(row['combined_score']),combined,abs_tol=1e-10)
        records.append({'case_id':cid,'score':combined,'valid':valid,'strict':strict,'both':strict and valid,
                        'dimensions':averages,'channel_scores':[sa/100,sb/100],
                        'channel_strict':[sa>=400 and min(a)>=3,sb>=400 and min(b)>=3],
                        'disagreement':abs(sa-sb)>=100,
                        'legacy_disagreement_mismatch':truth(row['expert_disagreement'])!=(abs(sa-sb)>=100),
                        'legacy_e2e_differs_from_strict':truth(row['end_to_end_usable'])!=(strict and valid)})
    assert len(records)==459
    n=len(records);p1=mean(r['channel_strict'][0] for r in records);p2=mean(r['channel_strict'][1] for r in records)
    agreement=mean(r['channel_strict'][0]==r['channel_strict'][1] for r in records)
    chance=p1*p2+(1-p1)*(1-p2)
    count=lambda predicate:sum(predicate(r) for r in records)
    summary={'n':n,'mean':mean(r['score'] for r in records),
             'valid':count(lambda r:r['valid']),'strict':count(lambda r:r['strict']),'both':count(lambda r:r['both']),
             'validator_only':count(lambda r:r['valid'] and not r['strict']),
             'semantic_only':count(lambda r:r['strict'] and not r['valid']),
             'neither':count(lambda r:not r['strict'] and not r['valid']),
             'dimension_means':{d:mean(r['dimensions'][j] for r in records) for j,d in enumerate(dims)},
             'icc2_1':icc([r['channel_scores'] for r in records]),'kappa':(agreement-chance)/(1-chance) if chance<1 else None,
             'disagreement':count(lambda r:r['disagreement']),
             'disagreement_flag_mismatches':[r['case_id'] for r in records if r['legacy_disagreement_mismatch']],
             'stored_end_to_end_mismatches':count(lambda r:r['legacy_e2e_differs_from_strict']),
             'score_bins':[count(lambda r:r['score']<3),count(lambda r:3<=r['score']<4),
                           count(lambda r:4<=r['score']<4.5),count(lambda r:r['score']>=4.5)]}
    for key in ('valid','strict','both','validator_only','semantic_only','neither','disagreement'):summary[key+'_pct']=100*summary[key]/n
    summary['strict_given_valid_pct']=100*summary['both']/summary['valid']
    summary['valid_given_strict_pct']=100*summary['both']/summary['strict']
    return summary,records

def write_csv(path,rows):
    assert rows
    with path.open('w',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)

def main():
    manifest=json.loads((ROOT/'data/source_manifest.json').read_text(encoding='utf-8'))
    paths=[ROOT/v for v in manifest['runs'].values()]+[ROOT/v for v in manifest['ratings'].values()]+[ROOT/manifest['protocol']]
    runs={};stats={};subsets={}
    for key,relative in manifest['runs'].items():
        rows=json.loads((ROOT/relative).read_text(encoding='utf-8'))
        run={f"Case{int(r['case_num']):03d}":r for r in rows}
        assert len(rows)==len(run)==459
        assert set(run)=={f'Case{n:03d}' for n in range(1,460)}
        for r in rows:
            assert isinstance(r['success'],bool)
            for val in (r['runtime'],r['token_stats']['total_tokens']):
                assert isinstance(val,(int,float)) and not isinstance(val,bool) and math.isfinite(val) and val>=0
            rc=r['repair_count'];assert rc is None or isinstance(rc,int) and not isinstance(rc,bool) and 0<=rc<=5
        runs[key]=run;stats[key]=aggregate(rows)
        if key in ('full','direct'):
            for subset,pred in [('existing',lambda n:n<=60),('constructed',lambda n:n>60)]:
                subsets[key+'_'+subset]=aggregate([r for r in rows if pred(int(r['case_num']))])
    tree=ast.parse((ROOT/manifest['protocol']).read_text(encoding='utf-8-sig'))
    weights=next(ast.literal_eval(node.value) for node in tree.body if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='WEIGHTS' for t in node.targets))
    read=lambda relative:list(csv.DictReader((ROOT/relative).open(encoding='utf-8-sig',newline='')))
    rq1=read(manifest['ratings']['rq1']);rq3=read(manifest['ratings']['rq3'])
    assert len(rq1)==918 and len(rq3)==2295
    experts={};ratings={}
    for key,tag in [('full','A'),('direct','B')]:experts[key],ratings[key]=assess([r for r in rq1 if r['setting']==tag],runs[key],weights)
    for key,model in MODEL_NAMES.items():
        summary,records=assess([r for r in rq3 if r['model']==model],runs[key],weights)
        if key=='full':assert sorted(records,key=lambda r:r['case_id'])==sorted(ratings[key],key=lambda r:r['case_id'])
        else:experts[key]=summary;ratings[key]=records
    f=runs['full'];b=runs['direct'];both=sum(f[c]['success'] and b[c]['success'] for c in f)
    n10=sum(f[c]['success'] and not b[c]['success'] for c in f);n01=sum(not f[c]['success'] and b[c]['success'] for c in f)
    discordant=n10+n01
    p=min(1,2*sum(math.comb(discordant,j) for j in range(min(n10,n01)+1))/(1<<discordant)) if discordant else 1
    paired={'both':both,'full_only':n10,'direct_only':n01,'neither':459-both-n10-n01,
            'odds_ratio':n10/n01 if n01 else None,'exact_mcnemar_p':p}
    out=ROOT/'data/statistics';out.mkdir(parents=True,exist_ok=True)
    for name,obj in [('stats',stats),('experts',experts),('paired',paired),('subsets',subsets),('weights',weights)]:
        (out/(name+'.json')).write_text(json.dumps(obj,indent=2,ensure_ascii=False,allow_nan=False)+'\n',encoding='utf-8')
    write_csv(out/'run_summary.csv',[{'run':k,**{x:v for x,v in s.items() if not isinstance(v,dict)}} for k,s in stats.items()])
    write_csv(out/'expert_summary.csv',[{'run':k,**{x:v for x,v in s.items() if not isinstance(v,(dict,list))}} for k,s in experts.items()])
    write_csv(out/'expert_case_scores.csv',[{'run':k,**{x:v for x,v in r.items() if not isinstance(v,list)}} for k,rs in ratings.items() for r in rs])
    hashes=[{'file':os.path.relpath(p,ROOT).replace('\\','/'),
             'sha256':hashlib.sha256(p.read_bytes().replace(b'\r\n',b'\n')).hexdigest(),
             'normalization':'CRLF to LF'} for p in paths]
    (out/'input_hashes.json').write_text(json.dumps(hashes,indent=2)+'\n',encoding='utf-8')
    print(f'PASS: {len(runs)} configurations, {sum(len(r) for r in runs.values())} cases, {sum(len(r) for r in ratings.values())} unique scored artifacts.')

if __name__=='__main__':main()
