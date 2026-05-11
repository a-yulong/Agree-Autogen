# Attention Defensive Rules

???? Attention.txt ?? AGREE ???????????? Kdef ??????????? artifact ?????????

## kdef.attention.1 鍙橀噺澹版槑瑙勫垯

- ???`general_defensive_rule`
- ???Attention.txt

鍙橀噺澹版槑瑙勫垯

## kdef.attention.1_1 鎵€鏈夊湪 annex agree {** ... **} 涓娇鐢ㄧ殑鍐呴儴鍙橀噺锛堥潪绔彛锛夊繀椤婚€氳繃 eq

- ???`declaration_and_assignment`
- ???Attention.txt

鎵€鏈夊湪 annex agree {** ... **} 涓娇鐢ㄧ殑鍐呴儴鍙橀噺锛堥潪绔彛锛夊繀椤婚€氳繃 eq 鏄惧紡澹版槑锛屽苟鎸囧畾绫诲瀷锛堝 real, bool, int锛?涓ョ鍑虹幇浠讳綍涓嶄互 eq銆乧onst銆乤ssume 鎴?guarantee 寮€澶寸殑瀛ょ珛璧嬪€艰鍙ャ€?

## kdef.attention.1_2 绂佹鐢?eq 澹版槑宸插湪缁勪欢 features 涓畾涔夌殑绔彛鍚嶇О锛堝 outACLVV锛夈€傜郴缁熺鍙?

- ???`declaration_and_assignment`
- ???Attention.txt

绂佹鐢?eq 澹版槑宸插湪缁勪欢 features 涓畾涔夌殑绔彛鍚嶇О锛堝 outACLVV锛夈€傜郴缁熺鍙ｅ湪 AGREE 涓嚜鍔ㄥ彲瑙侊紝閲嶅澹版槑浼氬鑷村懡鍚嶅啿绐侀敊璇€?

## kdef.attention.1_3 鑷畾涔夋暟鎹被鍨嬬殑鍘熷瓙鍛介鍙橀噺锛屼篃闇€鍏堥€氳繃 eq 鍦ㄥ搴?annex 涓樉寮忓０鏄庛€?

- ???`declaration_and_assignment`
- ???Attention.txt

鑷畾涔夋暟鎹被鍨嬬殑鍘熷瓙鍛介鍙橀噺锛屼篃闇€鍏堥€氳繃 eq 鍦ㄥ搴?annex 涓樉寮忓０鏄庛€?

## kdef.attention.1_4 缁欑鍙ｈ瀹氬浐瀹氬€硷紝鐩存帴鍦ㄥ疄鐜板眰鐨?assign 涓祴鍊?

- ???`declaration_and_assignment`
- ???Attention.txt

缁欑鍙ｈ瀹氬浐瀹氬€硷紝鐩存帴鍦ㄥ疄鐜板眰鐨?assign 涓祴鍊?

## kdef.attention.2 鑷畾涔夊熀纭€绫诲瀷瀹氫箟锛堝繀椤诲湪 AGREE 澶栭儴锛?

- ???`package_and_reference`
- ???Attention.txt

鑷畾涔夊熀纭€绫诲瀷瀹氫箟锛堝繀椤诲湪 AGREE 澶栭儴锛?
鑻ュ湪 AGREE 涓娇鐢?int / real / bool锛岄渶鍦ㄥ寘锛坧ackage锛夊眰绾у畾涔夊搴?AADL 鏁版嵁绫诲瀷锛?
data int extends Base_Types::Integer
end int;
data real extends Base_Types::Float
end real;
data bool extends Base_Types::Boolean
end bool;

## kdef.attention.3 with 寮曠敤瑕佹眰

- ???`package_and_reference`
- ???Attention.txt

with 寮曠敤瑕佹眰
浠讳綍浣跨敤 :: 鐨勮娉曪紙濡?Base_Types::Float锛夛紝蹇呴』鍦ㄦ枃浠跺紑澶撮€氳繃 with 寮曞叆瀵瑰簲鍖咃細with Base_Types;

## kdef.attention.3_1 AADL浠ｇ爜璺ㄥ寘寮曠敤浣跨敤鐐瑰紩鐢紝濡傦細gcas.timeToRecovery锛?

- ???`general_defensive_rule`
- ???Attention.txt

AADL浠ｇ爜璺ㄥ寘寮曠敤浣跨敤鐐瑰紩鐢紝濡傦細gcas.timeToRecovery锛?

## kdef.attention.3_2 鑰屽叾涓殑agree annex浠ｇ爜璺ㄥ寘寮曠敤涓嶅悓锛屽繀椤讳娇鐢ㄥ弻鍐掑彿"

- ???`package_and_reference`
- ???Attention.txt

鑰屽叾涓殑agree annex浠ｇ爜璺ㄥ寘寮曠敤涓嶅悓锛屽繀椤讳娇鐢ㄥ弻鍐掑彿"::" 绗﹀彿寮曠敤锛屽锛歅ackageName::VariableName

## kdef.attention.4 Annex 鎻掑叆浣嶇疆瑙勫垯

- ???`scope_and_placement`
- ???Attention.txt

Annex 鎻掑叆浣嶇疆瑙勫垯

## kdef.attention.4_1 eq 鍙橀噺銆乧onst 甯搁噺銆乤ssume/guarantee鐨勬彃鍏ヤ綅缃細鍙兘鍑虹幇鍦ㄧ粍浠剁被鍨嬶紙c

- ???`declaration_and_assignment`
- ???Attention.txt

eq 鍙橀噺銆乧onst 甯搁噺銆乤ssume/guarantee鐨勬彃鍏ヤ綅缃細鍙兘鍑虹幇鍦ㄧ粍浠剁被鍨嬶紙component type锛夊唴閮紝浣嶄簬 features/properties 涔嬪悗锛宔nd component; 涔嬪墠銆備笉鑳藉嚭鐜板湪 implementation 涓€?

## kdef.attention.4_2 assign銆乴emma璇彞鐨勬彃鍏ヤ綅缃細浠呭厑璁稿湪缁勪欢瀹炵幇锛坈omponent implement

- ???`declaration_and_assignment`
- ???Attention.txt

assign銆乴emma璇彞鐨勬彃鍏ヤ綅缃細浠呭厑璁稿湪缁勪欢瀹炵幇锛坈omponent implementation锛夊唴閮紝浣嶄簬 subcomponents/connections 涔嬪悗锛宔nd component.impl; 涔嬪墠

## kdef.attention.5 assign 璇彞鐨勫乏鍊煎繀椤绘槸棰勫厛瀛樺湪鐨勶紝瑕佷箞鏄湪 features 涓畾涔夌殑杈撳嚭绔彛锛岃涔堟槸鍦?

- ???`declaration_and_assignment`
- ???Attention.txt

assign 璇彞鐨勫乏鍊煎繀椤绘槸棰勫厛瀛樺湪鐨勶紝瑕佷箞鏄湪 features 涓畾涔夌殑杈撳嚭绔彛锛岃涔堟槸鍦ㄧ粍浠剁被鍨嬩腑閫氳繃 eq 澹版槑杩囩殑鍙橀噺锛涚姝㈠湪瀹炵幇灞傞€氳繃 assign 鐩存帴鍒涘缓鏂板彉閲?

## kdef.attention.6 閫昏緫杩愮畻绗︿娇鐢細and锛堜笌锛塷r锛堟垨锛塶ot(...)锛堥潪锛夛紱绂佹浣跨敤 C/Java 椋庢牸绗﹀彿锛?

- ???`general_defensive_rule`
- ???Attention.txt

閫昏緫杩愮畻绗︿娇鐢細and锛堜笌锛塷r锛堟垨锛塶ot(...)锛堥潪锛夛紱绂佹浣跨敤 C/Java 椋庢牸绗﹀彿锛?&, ||, !

## kdef.attention.7 绂佹浣跨敤鐨勭鍙蜂笌璇彞锛氱姝㈠紩鍏ラ潪鏍囧噯绗﹀彿锛氣垉, 鈭€, 鈭? 鈼? 鈻?绛?

- ???`general_defensive_rule`
- ???Attention.txt

绂佹浣跨敤鐨勭鍙蜂笌璇彞锛氱姝㈠紩鍏ラ潪鏍囧噯绗﹀彿锛氣垉, 鈭€, 鈭? 鈼? 鈻?绛?

## kdef.attention.8 assume / guarantee /assign 鍙婂叾浠栨爣绛惧悕鐨勬爣绛惧悕蹇呴』鐢ㄥ弻寮曞彿鎷捣锛屽锛?

- ???`declaration_and_assignment`
- ???Attention.txt

assume / guarantee /assign 鍙婂叾浠栨爣绛惧悕鐨勬爣绛惧悕蹇呴』鐢ㄥ弻寮曞彿鎷捣锛屽锛歡uarantee "safe after recovery": ... ;

## kdef.attention.9 璧嬪€艰鍙?

- ???`general_defensive_rule`
- ???Attention.txt

璧嬪€艰鍙?

## kdef.attention.9_1 璧嬪€间娇鐢?=锛岀姝娇鐢?

- ???`general_defensive_rule`
- ???Attention.txt

璧嬪€间娇鐢?=锛岀姝娇鐢?:=

## kdef.attention.9_2 璧嬪€艰鍙ュ乏鍙充袱渚х被鍨嬪繀椤讳竴鑷?鏁板€煎彉閲忥紙濡?real锛夊彸渚у繀椤绘槸鏁板€艰〃杈惧紡锛堝父閲忋€佸彉閲忋€佺畻鏈繍绠?

- ???`declaration_and_assignment`
- ???Attention.txt

璧嬪€艰鍙ュ乏鍙充袱渚х被鍨嬪繀椤讳竴鑷?鏁板€煎彉閲忥紙濡?real锛夊彸渚у繀椤绘槸鏁板€艰〃杈惧紡锛堝父閲忋€佸彉閲忋€佺畻鏈繍绠楋級,绂佹灏嗛€昏緫琛ㄨ揪寮忥紙杩斿洖 bool锛夎祴鍊肩粰鏁板€煎彉閲?
绀轰緥锛?
--  閿欒
eq danger : real = (altitude < 30);  -- 绫诲瀷涓嶅尮閰嶏紒
--姝ｇ‘锛堣嫢闇€甯冨皵鍙橀噺锛?
eq danger : bool = (altitude < 30);

## kdef.attention.10 姣旇緝杩愮畻绗︼紙>, <, >= 绛夛級杩斿洖 bool锛屼笉鍙洿鎺ョ敤浜庢暟鍊艰祴鍊笺€?

- ???`general_defensive_rule`
- ???Attention.txt

姣旇緝杩愮畻绗︼紙>, <, >= 绛夛級杩斿洖 bool锛屼笉鍙洿鎺ョ敤浜庢暟鍊艰祴鍊笺€?

## kdef.attention.11 AGREE瑙勭害鐢熸垚鍐呭蹇呴』浣撶幇 鈥滆Е鍙戞潯浠?鈫?鏃堕棿绾︽潫 鈫?鐩爣琛屼负鈥?鐨勫畬鏁撮€昏緫閾?

- ???`general_defensive_rule`
- ???Attention.txt

AGREE瑙勭害鐢熸垚鍐呭蹇呴』浣撶幇 鈥滆Е鍙戞潯浠?鈫?鏃堕棿绾︽潫 鈫?鐩爣琛屼负鈥?鐨勫畬鏁撮€昏緫閾?

## kdef.attention.11_1 鎺ㄨ崘鍖呭惈鏃堕棿鑼冨洿涓庡姩鎬佽涓恒€備緥濡傦細guarantee "climb after gcas"

- ???`declaration_and_assignment`
- ???Attention.txt

鎺ㄨ崘鍖呭惈鏃堕棿鑼冨洿涓庡姩鎬佽涓恒€備緥濡傦細guarantee "climb after gcas":
gcasRequested -> (t >= timeToRecovery => outACLVV > 0.0);

## kdef.attention.11_2 閬垮厤浠呭啓鎶借薄閫昏緫锛堝 A and B => C 鑰屾棤鏃堕棿鎴栫姸鎬佹紨杩涳級

- ???`logic_and_type`
- ???Attention.txt

閬垮厤浠呭啓鎶借薄閫昏緫锛堝 A and B => C 鑰屾棤鏃堕棿鎴栫姸鎬佹紨杩涳級

## kdef.attention.12 鎵€鏈夊熀浜?pre() 鐨勭姸鎬侀€掓帹锛堝鏃堕棿 t銆佷綅绉?s锛夊繀椤诲湪 system 绫诲瀷鐨?eq 璇彞

- ???`declaration_and_assignment`
- ???Attention.txt

鎵€鏈夊熀浜?pre() 鐨勭姸鎬侀€掓帹锛堝鏃堕棿 t銆佷綅绉?s锛夊繀椤诲湪 system 绫诲瀷鐨?eq 璇彞涓€氳繃 -> 绠楀瓙涓€娆℃€ч棴鐜畾涔夛紙濡?eq t : real = 0.0 -> pre(t) + 1.0;锛夛紝绂佹灏嗗垵濮嬪€煎啓鍦?assume 閲屾垨灏嗛€掓帹杩囩▼鍐欏湪 assign 閲?

## kdef.attention.13 甯搁噺瀹氫箟锛氬浐瀹氶槇鍊煎繀椤荤敤 const 澹版槑銆傜ず渚嬶細const low_altitude_thre

- ???`declaration_and_assignment`
- ???Attention.txt

甯搁噺瀹氫箟锛氬浐瀹氶槇鍊煎繀椤荤敤 const 澹版槑銆傜ず渚嬶細const low_altitude_threshold : real = 30.0;
const time_step : real = 0.001;

## kdef.attention.14 鍙橀噺鍏宠仈鎬э細

- ???`general_defensive_rule`
- ???Attention.txt

鍙橀噺鍏宠仈鎬э細

## kdef.attention.14_1 鎵€鏈?assume/guarantee 涓殑鍙橀噺锛屽繀椤诲叧鑱?AADL 妯″瀷涓殑缁勪欢銆佺鍙ｃ€佸瓙绋嬪簭

- ???`general_defensive_rule`
- ???Attention.txt

鎵€鏈?assume/guarantee 涓殑鍙橀噺锛屽繀椤诲叧鑱?AADL 妯″瀷涓殑缁勪欢銆佺鍙ｃ€佸瓙绋嬪簭鎴栧唴閮ㄧ姸鎬併€?

## kdef.attention.14_2 绂佹鍑虹幇瀛ょ珛鍙橀噺鎴栨棤鏉ユ簮鐨勯粯璁ゅ€?

- ???`general_defensive_rule`
- ???Attention.txt

绂佹鍑虹幇瀛ょ珛鍙橀噺鎴栨棤鏉ユ簮鐨勯粯璁ゅ€?

## kdef.attention.15 楂橀閿欒姹囨€?

- ???`general_defensive_rule`
- ???Attention.txt

楂橀閿欒姹囨€?

## kdef.attention.15_1 assume 鍜?guarantee 璇彞蹇呴』鍖呭惈鍞竴鐨勩€佸甫鍙屽紩鍙风殑瀛楃涓叉爣绛撅紙濡?assume

- ???`logic_and_type`
- ???Attention.txt

assume 鍜?guarantee 璇彞蹇呴』鍖呭惈鍞竴鐨勩€佸甫鍙屽紩鍙风殑瀛楃涓叉爣绛撅紙濡?assume "label": expression;

## kdef.attention.15_2 assume 璇彞涓嶅彲鍑虹幇鍦ㄧ粍浠跺疄鐜帮紙implementation锛変腑

- ???`scope_and_placement`
- ???Attention.txt

assume 璇彞涓嶅彲鍑虹幇鍦ㄧ粍浠跺疄鐜帮紙implementation锛変腑

## kdef.attention.15_3 蹇呴』鏄惧紡寮曠敤鎵€渚濊禆鐨勫寘

- ???`general_defensive_rule`
- ???Attention.txt

蹇呴』鏄惧紡寮曠敤鎵€渚濊禆鐨勫寘

## kdef.attention.15_4 閫昏緫杩愮畻绗﹀繀椤讳娇鐢?AGREE 鏍囧噯璇硶

- ???`general_defensive_rule`
- ???Attention.txt

閫昏緫杩愮畻绗﹀繀椤讳娇鐢?AGREE 鏍囧噯璇硶

## kdef.attention.15_5 assign 璇彞鍙兘鍑虹幇鍦ㄧ粍浠跺疄鐜扮殑 annex 涓?绂佹鍦ㄥ疄鐜板眰閫氳繃 assign 鐩存帴鍒涘缓

- ???`declaration_and_assignment`
- ???Attention.txt

assign 璇彞鍙兘鍑虹幇鍦ㄧ粍浠跺疄鐜扮殑 annex 涓?绂佹鍦ㄥ疄鐜板眰閫氳繃 assign 鐩存帴鍒涘缓鏂板彉閲忥紝涓斾弗绂佸宸插湪 eq 涓畬鎴愬畾涔夌殑鍙橀噺杩涜浜屾 assign.

## kdef.attention.16 鍦?guarantee 涓紝浣跨敤 鍗曞悜钑村惈 => 琛ㄨ揪鈥滆嫢鏉′欢鎴愮珛锛屽垯缁撴灉蹇呴』鎴愮珛鈥?涓嶄娇鐢ㄥ弻鍚?

- ???`logic_and_type`
- ???Attention.txt

鍦?guarantee 涓紝浣跨敤 鍗曞悜钑村惈 => 琛ㄨ揪鈥滆嫢鏉′欢鎴愮珛锛屽垯缁撴灉蹇呴』鎴愮珛鈥?涓嶄娇鐢ㄥ弻鍚戣暣鍚?<->

## kdef.attention.17 AGREE 涓嶆敮鎸佷换浣曞唴缃殑鏁板搴撳嚱鏁帮紙濡?min, max, abs, sqrt, sin 绛?

- ???`logic_and_type`
- ???Attention.txt

AGREE 涓嶆敮鎸佷换浣曞唴缃殑鏁板搴撳嚱鏁帮紙濡?min, max, abs, sqrt, sin 绛夛級锛涢櫎鍩虹绠楁湳鍜岄€昏緫杩愮畻澶栵紝鎵€鏈夐€夋嫨閫昏緫蹇呴』閫氳繃 if-then-else 鏉′欢琛ㄨ揪寮忔樉寮忓疄鐜?

## kdef.attention.18 蹇呴』灏?AGREE 鍙橀噺涓?AADL 妯″瀷涓殑瀹為檯鍏冪礌锛堝瀛愮粍浠惰緭鍑恒€佺鍙ｅ€硷級缁戝畾

- ???`general_defensive_rule`
- ???Attention.txt

蹇呴』灏?AGREE 鍙橀噺涓?AADL 妯″瀷涓殑瀹為檯鍏冪礌锛堝瀛愮粍浠惰緭鍑恒€佺鍙ｅ€硷級缁戝畾

## kdef.attention.19 AGREE annex涓嶅厑璁稿湪assume/guarantee涓紩鐢ㄤ换浣曞瓙缁勪欢.瀛愮粍浠剁粦瀹氬彧鑳藉湪

- ???`declaration_and_assignment`
- ???Attention.txt

AGREE annex涓嶅厑璁稿湪assume/guarantee涓紩鐢ㄤ换浣曞瓙缁勪欢.瀛愮粍浠剁粦瀹氬彧鑳藉湪assign 涓畬鎴?

## kdef.attention.19_1 鍗充娇瀛愮粍浠跺悕绉板湪褰撳墠浣滅敤鍩熲€滅湅璧锋潵鍙鈥濓紝鍙鍦?component 灞傦紝灏变笉鑳藉紩鐢ㄥ畠浠€?

- ???`scope_and_placement`
- ???Attention.txt

鍗充娇瀛愮粍浠跺悕绉板湪褰撳墠浣滅敤鍩熲€滅湅璧锋潵鍙鈥濓紝鍙鍦?component 灞傦紝灏变笉鑳藉紩鐢ㄥ畠浠€?

## kdef.attention.19_2 閫氳繃 assign 灏嗚繖浜涘唴閮ㄥ彉閲忕粦瀹氬埌瀹為檯瀛愮粍浠剁鍙ｏ紝杩欎簺鍙橀噺闇€瑕佸湪Component涓€氳繃

- ???`declaration_and_assignment`
- ???Attention.txt

閫氳繃 assign 灏嗚繖浜涘唴閮ㄥ彉閲忕粦瀹氬埌瀹為檯瀛愮粍浠剁鍙ｏ紝杩欎簺鍙橀噺闇€瑕佸湪Component涓€氳繃 eq 澹版槑銆?

## kdef.attention.20 姣忎釜 annex agree 鍧楃殑浣滅敤鍩熶粎闄愪簬鍏舵墍鍦ㄧ殑 缁勪欢瀹氫箟涓婁笅鏂?鍦?system X锛堢被

- ???`declaration_and_assignment`
- ???Attention.txt

姣忎釜 annex agree 鍧楃殑浣滅敤鍩熶粎闄愪簬鍏舵墍鍦ㄧ殑 缁勪欢瀹氫箟涓婁笅鏂?鍦?system X锛堢被鍨嬶級涓０鏄庣殑 eq 鍙橀噺锛屽湪 system implementation X.impl 鐨?annex 涓笉鍙

## kdef.attention.21 閬垮厤鍦?system implementation 涓娇鐢?assign 缁戝畾瀛愮粍浠剁鍙ｅ埌鑷韩绔?

- ???`declaration_and_assignment`
- ???Attention.txt

閬垮厤鍦?system implementation 涓娇鐢?assign 缁戝畾瀛愮粍浠剁鍙ｅ埌鑷韩绔彛

## kdef.attention.22 浜屽厓杩愮畻锛堝 +, -, *, /, >, = 绛夛級鐨勫乏鍙虫搷浣滄暟蹇呴』鍏锋湁瀹屽叏鐩稿悓鐨勭被鍨?

- ???`general_defensive_rule`
- ???Attention.txt

浜屽厓杩愮畻锛堝 +, -, *, /, >, = 绛夛級鐨勫乏鍙虫搷浣滄暟蹇呴』鍏锋湁瀹屽叏鐩稿悓鐨勭被鍨?

## kdef.attention.23 pre 璇彞浣跨敤蹇呴』鍜岋紙锛夋惌閰嶏紝渚嬪锛歱re (t)锛?涓嶅厑璁革細pre t锛?

- ???`logic_and_type`
- ???Attention.txt

pre 璇彞浣跨敤蹇呴』鍜岋紙锛夋惌閰嶏紝渚嬪锛歱re (t)锛?涓嶅厑璁革細pre t锛?

## kdef.attention.24 褰撳湪鏌愮粍浠跺紩鐢ㄥ彟涓€涓瓙缁勪欢鐨勭鍙ｆ椂锛岃瀛愮粍浠剁殑 implementation 蹇呴』鍖呭惈鑷冲皯涓€涓?

- ???`scope_and_placement`
- ???Attention.txt

褰撳湪鏌愮粍浠跺紩鐢ㄥ彟涓€涓瓙缁勪欢鐨勭鍙ｆ椂锛岃瀛愮粍浠剁殑 implementation 蹇呴』鍖呭惈鑷冲皯涓€涓?annex agree 鍧楋紙鍐呭鍙负绌猴級銆?

## kdef.attention.25 涓ョ瀵瑰悓涓€涓彉閲忓悓鏃朵娇鐢?eq 璧嬪€煎畾涔夊拰 assign 璧嬪€煎畾涔夈€?

- ???`declaration_and_assignment`
- ???Attention.txt

涓ョ瀵瑰悓涓€涓彉閲忓悓鏃朵娇鐢?eq 璧嬪€煎畾涔夊拰 assign 璧嬪€煎畾涔夈€?

## kdef.attention.25_1 鑻ュ彉閲忓湪缁勪欢绫诲瀷锛圫ystem Type锛変腑宸查€氳繃 eq 鍙橀噺鍚?

- ???`declaration_and_assignment`
- ???Attention.txt

鑻ュ彉閲忓湪缁勪欢绫诲瀷锛圫ystem Type锛変腑宸查€氳繃 eq 鍙橀噺鍚?: 绫诲瀷 = 琛ㄨ揪寮?锛堝寘鍚瓑鍙凤級瀹屾垚浜嗗畾涔?

## kdef.attention.25_2 鍒欎弗绂佸湪瀹炵幇灞傦紙Implementation锛変腑瀵规鍙橀噺鍐嶆浣跨敤 assign

- ???`declaration_and_assignment`
- ???Attention.txt

鍒欎弗绂佸湪瀹炵幇灞傦紙Implementation锛変腑瀵规鍙橀噺鍐嶆浣跨敤 assign
姝ｇ‘鍋氭硶锛?
鏂瑰紡涓€锛圱ype灞傚畬鎴愶級锛歟q x : int = 5;锛圛mpl灞備笉鍑嗗啓 assign锛夈€?
鏂瑰紡浜岋紙Impl灞傚畬鎴愶級锛歟q x : int;锛圱ype灞備笉缁欑瓑鍙凤級 + assign x = 5;锛圛mpl灞傚畾涔夛級銆?

## kdef.attention.26 搴斾娇鐢ㄥ嵆鏃堕€昏緫鍏崇郴 => 鏉ユ弿杩版瘡涓€鏃跺埢鐨勫畨鍏ㄦ€т繚璇?涓嶆敮鎸?is_int 绫诲瀷鐨勮繍琛屾椂绫诲瀷妫€鏌?

- ???`logic_and_type`
- ???Attention.txt

搴斾娇鐢ㄥ嵆鏃堕€昏緫鍏崇郴 => 鏉ユ弿杩版瘡涓€鏃跺埢鐨勫畨鍏ㄦ€т繚璇?涓嶆敮鎸?is_int 绫诲瀷鐨勮繍琛屾椂绫诲瀷妫€鏌ワ紝涓斾笉鏀寔 eventually 绛?LTL 娲诲害绠楀瓙銆?

## kdef.attention.27 鍒嗘敮閫夋嫨閫昏緫蹇呴』浣跨敤宓屽鐨?if ... then ... else,涓ョ浣跨敤 elsif 鍏抽敭

- ???`logic_and_type`
- ???Attention.txt

鍒嗘敮閫夋嫨閫昏緫蹇呴』浣跨敤宓屽鐨?if ... then ... else,涓ョ浣跨敤 elsif 鍏抽敭瀛?
