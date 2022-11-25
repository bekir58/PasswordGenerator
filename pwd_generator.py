# -*- coding: utf-8 -*-
"""

@author: bekir

"""

import string 
import random 



while True:
    
    print ("**********************************")
    print ("--------Password Generator--------")
    
    
    length  = int (input("Geben Sie bitte gewünschte länge der Password ein: "))
    
    inhalt = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    
    my_random = random.sample(inhalt, length)
    
    password = "".join(my_random)
    
    print (password)
    break
