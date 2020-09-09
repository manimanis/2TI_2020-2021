from random import randint

equipes = ['' for _ in range(2)]
equipes[0] = input('Nom 1ère équipe : ')
equipes[1] = input('Nom 2ème équipe : ')

faces = ['Pile', 'Face']

cap_eq = randint(0, 1)
print("Le capitaine de l'équipe", equipes[cap_eq], 'choisit Pile/Face')
cap_c = int(input('0: Pile, 1: Face ? '))
print("Le capitaine de l'équipe", equipes[cap_eq], "a choisi", faces[cap_c])

ts = randint(0, 1)
print("L'arbitre lance la pièce puis il l'attrape")
print("Résultat du tirage au sort :", faces[ts])

if ts == cap_c:
    nom_eq = equipes[cap_eq]
else:
    nom_eq = equipes[(cap_eq + 1) % 2]

print("Le ballon est en possession de l'équipe :", nom_eq)
