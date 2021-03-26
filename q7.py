#7. base_RSA: Maybe it's not 10 based number? what about base 4242?

from libnum import *
from sympy import nextprime
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
from pwn import *
from itertools import product
import random
from FLAG import flag

def backdoor42():
    return nextprime(pow(4242, 99) + random.randint(0, 4242) * pow(4242, 66) + random.randint(0, 4242) * pow(4242, 42))

p, q = backdoor42(), backdoor42()
n = p * q
e = nextprime(424242)#424243
print(f"n = {n}")
print(f"c = {pow(bytes_to_long(flag), e, n)}")


"""
output:
n = 18154801622837453511597027200273355126432183309343269831312913974774450879689157369432156314004912109838304209411540191206682093624302694926030891785750531749015878000196005499638209644341839368847784682996800412013879458911943107532762408700725068385755582489846988898364636200832966212063744336544785680165141552088776107067096307255009226424126056650977875748442589881960048206722165088216735514371255506193490862420820934223452208541575916070051217950438301819124828545547924370314422238516166212943891334827330477393250743242558706180459848483127761570022090010583359165321469021252001725102248978139834916314033525368707058111078235916690004878913678643169604535019899964885797068600508440033289768600852670499551
c = 4627263094019315952612016855232007095526525411374050410726840204376065685317150766031721652286334951612876451994079029202093795761210146277043886453255874914545386666507891340138245078224422144199804323075871451923492651217726286976398357189000555248126738667188192399665005770587464136768232215410828652509136178604602970325593814270793765304397621774810197551274147630157406255473172987016166983473194949973246151848116994350581011970923960660279060050698864890713374608643031085814986295564469806730206327940270828447978870986533919301259585331534875413468857321345616456144576378350614783084300237805242884655008003042349050083768865914380667608047829561883452073955257442194165133762967524633505641648762018508640
"""
