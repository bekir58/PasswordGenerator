# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 21:53:15 2022

@author: bekir
"""

import string 
import random 



while True:
    
    print ("**********************************")
    print ("--------Password Generator--------")
    
    
    länge = int (input("Wie lang soll Ihrer Password sein: "))
    
    inhalt = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    
    my_random = random.sample(inhalt, länge)
    
    password = "".join(my_random)
    
    print (password)
    break
