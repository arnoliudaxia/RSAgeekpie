#8. related message revenge: Simple related message attack

# First you need to download Crypto library!
import subprocess

###############################################################################
try:                                                                          #
    from Crypto.Util.number import *                                          #
except ImportError:                                                           #  DO NOT
    subprocess.check_call(['python', "-m", "pip", "install", 'PyCryptodome'], #
                          stdout=subprocess.DEVNULL,                          #  CHANGE
                          stderr=subprocess.DEVNULL)                          #
finally:                                                                      #
    from Crypto.Util.number import *                                          #
###############################################################################
from secret import flag

s1 = b'zyt'
s2 = b'ltt'

m1 = bytes_to_long(flag + b':' + s1)
m2 = bytes_to_long(flag + b':' + s2)

n = getPrime(512) * getPrime(512)
e = 0x2011

c1 = pow(m1, e, n)
c2 = pow(m2, e, n)

print(f"n = {n}")
print(f"c1 = {c1}")
print(f"c2 = {c2}")
"""
n = 100629568300195422026209720138083819740688937576398708400585960602682192936492818132466039511921120918016902172483760660489312630334139995305497444989216921549838520240791960625644839391829752509853217051446224001719653051737930338141651736504833754948493930878589007867644561521293569631611978825044223383791
c1 = 77153106333350149098279629783581253227714656776902515837639851310297008296341520748789739405907823190965742392321142798563704995011579576215915420935553294487314289721867798312847768689744803654287961656424428438670192770534776272801790345412123983823010056725849223104578367988324361061739199417023146339792
c2 = 6617950992311675687762501414795400646207381592567101754447321959539012263639850559149805006546049750372305353117122679938503745782131680133105798066991128043779095522514613143574582403794865963124469467543094080888707193448946337752273256302654241511325117016934545077200440220478972272488330644628023604051
"""