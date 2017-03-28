import numpy as np
import collections as c

###### Constant #####
nb_symbol = 26
######



def frequency(text,tab_lettre):
    taille=len(text)
    res = {}
    for lettre in tab_lettre:
        res[lettre]= 0
    for i in range(taille):
        if(text[i].isalpha()):
            res[text[i]]+= 1
    return sorted(res, key=res.__getitem__)
