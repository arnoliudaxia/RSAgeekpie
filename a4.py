from Crypto.Util.number import *
import gmpy2

d=57899763801722261062891290503559835904571946557258761154422546104824094670843
n = 1063045321283844468344531168992778520651192162100948533991539097447031440090068191835838938460807260866872379834796862916118785271062209281267667069640000501698142693389209275376843382863579650119977059768375028586326490055087394631528241983631462471709913758728591459476799115050977493979613545056736162868049
e = 837165022918376318972691589160491375229372195625940137121740685432530132860541010174727630660292946071507342455170833392895060048564125597915757582027572284342507277083636059558106672685400173531425920294781499112027917632497954958437660357575400222692979844873372105801998210845285775146263117399191185379347
c = 880629053111310380431098717985486426066883220269794468010063492039131202001984551004836644149273232622697784165926733617754388445388291866820628807996932264604209895417911536942313007315069213258166274848333187369750616282970776693830649350183644625611928987325168429535863220430105859871791370286307713251904


print(long_to_bytes(pow(c,d,n)).decode())