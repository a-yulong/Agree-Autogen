"""Re-extract measured fields from the public case reports and verify checksums.

Without --write this is a read-only integrity check. --write rebuilds the compact
JSON inputs; it never modifies source reports or ratings.
"""
from pathlib import Path
import argparse, hashlib, json

ROOT=Path(__file__).resolve().parents[1]
FIELDS=['case_num','success','repair_count','runtime','token_stats','stage_error']

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write',action='store_true')
    args=parser.parse_args()
    manifest=json.loads((ROOT/'data/source_manifest.json').read_text())
    sources=json.loads((ROOT/'data/source_reports.json').read_text())
    grouped={key:[] for key in manifest['runs']}
    for item in sources:
        p=ROOT.parent/item['source']
        if not p.is_file():raise FileNotFoundError(f'{p}: obtain the referenced reports with a full checkout or sparse checkout.')
        raw=p.read_bytes()
        # Git working trees may use CRLF; report hashes use repository LF bytes.
        raw=raw.replace(b'\r\n',b'\n')
        assert hashlib.sha256(raw).hexdigest()==item['sha256'],item['source']
        d=json.loads(raw.decode('utf-8-sig'))
        record={key:d.get(key) for key in FIELDS}
        record['source']='../'+item['source']
        grouped[item['run']].append(record)
    for key,records in grouped.items():
        assert len(records)==459
        target=ROOT/manifest['runs'][key]
        if args.write:target.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        else:assert json.loads(target.read_text(encoding='utf-8'))==records,key
    print(f'PASS: {len(sources)} source reports and {len(grouped)} extracted configurations.')

if __name__=='__main__':main()
