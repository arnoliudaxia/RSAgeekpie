'''
Created on Dec 14, 2011

@author: pablocelayes
'''
import Arithmetic
import ContinuedFractions
import RSAvulnerableKeyGenerator

n=64878819021798967882478794493169291798302120211275449746653428029794724742785633723640051659061856317816209582035259583556438660172294860460413134799333040033598536189843085939842357753841578416167271587296508846911245605654723770209659812751097002783783993725808670191173297930030108291570575974133212878301
e = 6030005108086807644065177174600396193324735278236942527236196183453936865303769715608170063667194028576668554175470112438766759369538269528025676262706968994771256981700477019524138154909880582993183751490133864993953996255549128686499929443419679109353124958757880828279023911982747870108602697045957004823


def hack_RSA(e,n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    frac = ContinuedFractions.rational_to_contfrac(e, n)
    convergents = ContinuedFractions.convergents_from_contfrac(frac)
    
    for (k,d) in convergents:
        
        #check if d is actually the key
        if k!=0 and (e*d-1)%k == 0:
            phi = (e*d-1)//k
            s = n - phi + 1
            # check if the equation x^2 - s*x + n = 0
            # has integer roots
            discr = s*s - 4*n
            if(discr>=0):
                t = Arithmetic.is_perfect_square(discr)
                if t!=-1 and (s+t)%2==0:
                    print("Hacked!")
                    return d

if __name__ == "__main__":
    print(hack_RSA(e,n))


    


        
    
