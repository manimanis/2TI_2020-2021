from random import randint

eq1 = input('Nom 1ère équipe : ')
eq2 = input('Nom 2ème équipe : ')

print('Le match est joué entre', eq1, 'et', eq2)

num_eq = randint(0, 1)
if num_eq == 0:
    eq = eq1
    autre_eq = eq2
else:
    eq = eq2
    autre_eq = eq1
print("Le capitaine de l'équipe", eq, 'choisit Pile/Face')

choix_cap = int(input('0: Pile, 1: Face ? '))
if choix_cap == 0:
    ch_cap = 'Pile'
else:
    ch_cap = 'Face'
print("Le capitaine de l'équipe", eq, "a choisi", ch_cap)

ts = randint(0, 1)
if ts == 0:
    face = 'Pile'
else:
    face = 'Face'

print("L'arbitre lance la pièce puis il l'attrape")
print("Résultat du tirage au sort :", face)

if ts == choix_cap:
    equipe = eq
else:
    equipe = autre_eq

print("Le ballon est en possession de l'équipe :", equipe)
