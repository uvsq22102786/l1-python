x = [3, 5, 10]
print(x)

x.extend([12, 17])
print(x)

p = x.index(10)
x[p] = -7 
print(x)

liste = [6, 10, -14, 24, 34] 

for i in range(len(liste)) : 
   liste[i] *= 2
print(liste)


import random 
liste_vide = []
for i in range(10):
    alea = random.randint(0, 100)
    liste_vide.append(alea) 
print(liste_vide)

import random 
liste_paire = []
liste_impaire = []
for i in range(10):
    alea = random.randint(0, 99)
    if alea % 2 == 0 :
        liste_paire.append(alea)
    else:
        liste_impaire.append(alea)

print("pair:",liste_paire)
print("impaire:", liste_impaire)


import random 
liste_croissante = []
for i in range(10):
    alea = random.randint(0, 100)
    liste_croissante.append(alea) 

liste_croissante.sort()
del liste_croissante[liste_croissante.index(min(liste_croissante))]
del liste_croissante[liste_croissante.index(max(liste_croissante))]
print(liste_croissante)

# autre variante :
#liste_croissante.sort(9)
#l2 = liste_croissante[1 : len(liste_croissante) -1]

#liste_croissante.sort()
#del liste_croissante[0]
#del liste_croissante[-1]
#print(liste_croissante)

carte = [i for i in range(1,53)]
print(carte)
##print(list(range(1,53)))
    
import random 
carte_coupe = []
for i in range (0, i - 1):
    i = random.randint(1,52)
    carte_coupe.append(i)
print(carte_coupe)

c = list(range(1,53))
i = random.randint(0,52)
r = c[i:] + c[:i]
print(r)

a1 = [1,2,3]
a2 = [3,4,5]

carre_mag = [a1, a2]

# ou
carre_mag1 = [[1,2,3],[3,4,5]]
carre_mag1 = [0][1]



liste = [6, 10, -14, 24, 34]

for i in range(len(liste)):
    liste[i] *= 2
print(liste)

for i in range(len(liste)):
    liste[i] += i 
print(liste)

import random 
liste_vide = []
for i in range (10):
    alea = random.randint(10,99)
    liste_vide.append(alea) 
print(liste_vide)


liste_paire2 = []
liste_impaire2 = []
for i in range(10):
    alea2 = random.randint(10,99)
    if alea % 2 == 0 :
        liste_paire2.append(alea2)
    else :
        liste_impaire2.append(alea2)
print("pair:",liste_paire2)
print("impaire:",liste_impaire2)