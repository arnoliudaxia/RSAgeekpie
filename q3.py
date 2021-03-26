#3. GCD_RSA: The generation of n1 and n2 seems insecure?
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
from FLAG import flag

"""
What's wrong with this RSA?
"""
m = bytes_to_long(flag)
p1 = getPrime(512)
p2 = getPrime(512)
q1 = q2 = getPrime(512)
n1 = p1 * q1
n2 = p2 * q2
e1 = getPrime(12)
e2 = getPrime(12)
c1 = pow(m, e1, n1)
c2 = pow(m, e2, n2)
print(f'n1 = {n1}')
print(f'n2 = {n2}')
print(f'c1 = {c1}')
print(f'c2 = {c2}')

"""
output:
n1 = 105859272580070028477768613935092051327162799887096690132148585164508660190502077441408404020409514340324369026785371773504206422556445918185198153596472346235516090426794892328531144231594915411374646896902090943592684202547452373340875912677575485519885709653812753267530809737552492437640139044382826300859
n2 = 96494486528299625440518542003702455509521231293161773217610734874836432448594274449004032101919378604475386300889713714018965977096817207788409315459505828748341261068404108336565749813982878179331324691645637281254005638732498062399530711063428144380312924720312891841039910542012065550177830136927997775277
c1 = 92553451561126713756643310047011524707013331647576401089256515795072089325219380724230208486189160235030539593208482741201639489601804354207444368225062781201156891043310125032651407627942128653511290372202273527375307380401695035542098553906197623239147027835738034975388599790034624519997540872985531154830
c2 = 210732714945847104156851338714107347163503660801575984230268104100841430051856748222279373525371693222371621022157051536525698392618113251258603304063847702009733545642872507313972967149744795121006224191371210569594639834534988115688873101994468720042568322913292150177556407751254321261277421667511072862
"""