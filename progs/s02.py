from random import randint

ne1 = input('Nom 1ère équipe : ')
ne2 = input('Nom 2ème équipe : ')

l_eq = [ne1, ne2]
faces = ['Pile', 'Face']

cap_eq = randint(0, 1)
print("Le capitaine de l'équipe", l_eq[cap_eq], 'choisit Pile/Face')
cap_c = int(input('0: Pile, 1: Face ? '))
print("Le capitaine de l'équipe", l_eq[cap_eq], "a choisi", faces[cap_c])

ts = randint(0, 1)
print("L'arbitre lance la pièce puis il l'attrape")
print("Résultat du tirage au sort :", faces[ts])

if ts == cap_c:
    nom_eq = l_eq[cap_eq]
else:
    nom_eq = l_eq[(cap_eq + 1) % 2]

print("Le ballon est en possession de l'équipe :", nom_eq)
