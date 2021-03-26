from Crypto.Util.number import *
import gmpy2

n=2911574709064212323855474227619822756130632228341898894819447416947891373259285826118379505207255455844257702726008662438786591052668400409760710601560660683550020886317998865684374425774612451145233336619342683455950907931145135089448704730972044313886518085826905863933632983268304654549529838865787867141562329
p=29017
q=100340307718379306056982948878926930976001386371502873998671379430950524632432223390370455429825807486792490702898599525753406315355426143631688685996507588088018088924354649539386374393445650864845895048397238979079536407317956201173405408242480074228435678596233444668078470664379662079109826614253295211137
c=1606213374164253323596861290758828696120183429733978683925445387571565721400672665596236912090816375896091946489042261227171182738465767763246930294884998654585254779679413113073615504522097221415773969471996754637934802454949236671242683577486308652883075258078877991814747634192130483256711936262319138177019291
e=65537


d = gmpy2.invert(e,(p-1)*(q-1))


print(long_to_bytes(pow(c,d,n)).decode())