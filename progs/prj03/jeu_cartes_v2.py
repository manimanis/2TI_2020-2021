from random import *

cartes = [0]

j1 = 0
j2 = 0
nbj1 = 0
nbj2 = 0
for i in range(1, 6):
    while j1 in cartes:
        j1 = randint(1, 10)
    cartes.append(j1)
    while j2 in cartes:
        j2 = randint(1, 10)
    cartes.append(j2)
    print("Joueur 1 a choisi :", j1)
    print("Joueur 2 a choisi :", j2)
    if j1 < j2:
        print("Joueur 1 gagne le tour num", i)
        nbj1 += 1
    else:
        print("Joueur 2 gagne le tour num", i)
        nbj2 += 1
if nbj1 > nbj2:
    print("Joueur 1 gagne la partie !")
else:
    print("Joueur 2 gagne la partie !")
