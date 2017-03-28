#CODE NON OPTIMISE !!!!!!!
import numpy as np
import sys
sys.path.append('C:/Users/arthu/Desktop/Programming/decode')
from frequency import *

#Defiition des constantes
nb_anglais = 26
tab_lettre = ['a','b','c','d','e','f','g','h',
                   'i','j','k','l','m','n','o','p',
                   'q','r','s','t','u','v','w','x',
                   'y','z']
tab_indice = {}
i=0
for lettre in tab_lettre:
    tab_indice[lettre]=i
    i += 1


infini = 100 #Nombre associé à un couple de lettre dont on est sure qu'il sont associés
#### Tableau des frequences des langues #####
frec = [8.08,1.67,3.18,3.99,12.56,2.17,1.80,5.27,7.24,0.14,
        0.63,4.04,2.30,7.38,7.47,1.91,0.09,6.42,6.59,9.15,
        2.79,1.00,1.89,0.21,1.65,0.07]

anglais = {}
i=0
for lettre in tab_lettre:
    anglais[lettre] = frec[i]
    i +=1

tab_anglais_sorted = sorted(anglais,key=anglais.__getitem__)


tab_connu = {'b':'e', 'j':'s', 'e':'n', 'p':'d', 'd':'y','f':'r', 'h':'b', 'k':'a', 'l':'c', 'o':'m', 'q':'l',
             'r':'o','t':'g', 'g':'u', 'n':'t', 'a':'i', 'w':'p', 'm':'v'}

def decode(file, tab_letter):
    #Ouverture fichier
    f=open(file,"r")
    contenu = f.read().casefold()
    #Traitement du texte

    map_assoc_lettre = {}
    for lettre in tab_lettre:
        map_assoc_lettre[lettre] = []

    for key, value in tab_connu.items():
        map_assoc_lettre[key].append(value)

    #Analyse frequentielle
    tab = frequency(contenu, tab_lettre)
    map_assoc_frequence = {}
    for i in range(nb_anglais):
        map_assoc_frequence[tab_anglais_sorted[i]] = tab[i]
        i += 1

    for key, value in map_assoc_frequence.items():
        map_assoc_lettre[key].append(value)

    print(map_assoc_lettre)
    tab_choisi = [False for i in range(nb_anglais)]
    map_final_assoc = {}
    for key, value in map_assoc_lettre.items():
        if( not(tab_choisi[tab_indice[value[0]]]) ):
            tab_choisi[tab_indice[value[0]]] = True
            map_final_assoc[key] = value[0]
        else:
            map_final_assoc[key] = value[0]

    print(map_final_assoc)
    #Recopie du message decodé
    decode = ''
    for letter in contenu:
        if(letter.isalpha()):
            decode += map_final_assoc[letter]
        else:
            decode += letter
    print(decode)
    f.close()
'''
f=open("test.txt","a")
for i in range(26):
    for j in range(i):
        f.write(tab_anglais[i])
f.close()
'''
#print(tab_anglais)
decode("test.txt", tab_anglais_sorted)

