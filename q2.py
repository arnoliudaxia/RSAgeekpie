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
###########################################################################
from sympy import *
from math import isqrt
from FLAG import flag

m = bytes_to_long(flag)

"""
[+] This time p and q are all big!!
[-] No no no, Femart thought that your RSA is easy to break! Because p and q are too near!! Femart can easily break it!
"""

p = getPrime(512)
q = nextprime(p)
n = p * q
e = 65537
c = pow(m, e, n)
print(f'n = {n}')
print(f'c = {c}')

"""
output:
n = 147423533891841436462912175767159449479164690919535569837654485357832966538291801352488874301685643654098601563811809560190294738158641898287196216011182646192371308106837722807188923322971282953291507774263875863165186981224356869255704056707354596409323760804018846628520021390433541542932398389899473923077
c = 70520353671114194316239067363406558212055364889803678911235327509893249117478393128464024877605231933530276915740444422461941958534514668237778704261826467426557603436031763832191564154655870220406926692032606937061851578303790344613239040030790950026641571282402030062732826755314763959324995616404599677928
"""