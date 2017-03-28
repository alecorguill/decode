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
for lettre in ['a','b','c','d','e','f','g','h','i','j',
               'k','l','m','n','o','p','q','r','s','t',
               'u','v','w','x','y','z']:
    anglais[lettre] = frec[i]
    i +=1

tab_anglais_sorted = sorted(anglais,key=anglais.__getitem__)


tab_connu = {'h':'h', 'o':'o', 'm':'m', 'y':'y'}
#Matrice M tk M[i][j] symbolise a quel point i et a de chance d'etre lié a j
def decode(file, tab_letter):
    #Ouverture fichier
    f=open(file,"r")
    contenu = f.read().casefold()
    #Traitement du texte

    #Remplie la matrice au endroit ou on est sure de l'association avec tab_connu
    mat_liaison = np.zeros((nb_anglais,nb_anglais))
    for key, value in tab_connu.items():
        mat_liaison[tab_indice[key]][tab_indice[value]] += infini

    #Analyse frequentielle
    tab = frequency(contenu, tab_lettre)
    map_assoc_frequence = {}
    for i in range(nb_anglais):
        map_assoc_frequence[tab_anglais_sorted[i]] = tab[i]
        i += 1

    for key, value in map_assoc_frequence.items():
        mat_liaison[tab_indice[key]][tab_indice[value]] += 10
        mat_liaison[tab_indice[value]][tab_indice[key]] += 10

    #Recopie du message decodé
    decode = ''
    for letter in contenu:
        if(letter.isalpha()):
            if(tab_connu.__contains__(letter)):
                decode += tab_connu[letter]
            else:
                decode += tab_anglais_sorted[tab.index(letter)]
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

