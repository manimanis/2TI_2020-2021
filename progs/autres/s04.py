from random import randint

# Saisie des noms des joueurs
print('Noms des joueurs')
nom_joueurs = []
for i in range(2):
    while True:
        nom = input(f'Nom du joueur n°{i+1} ? ')
        if nom != '':
            break
        print('Erreur: Entrer le nom du joueur')
    nom_joueurs.append(nom)

# Sélection de 5 nombres aléatoires de 1 à 20
nombres = []
for i in range(5):
    nombres.append(randint(4 * i + 1, 4 * (i+1)))

print(nombres)

# Le jeu se poursuit jusqu'à ce qu'un joueur
# découvre le dernier nombre
nj = 0
while len(nombres) != 0:
    print(f'Tour de {nom_joueurs[nj]}')
    while True:
        nbre = int(input('Entrer un nombre [1, 20] ? '))
        if 1 <= nbre <= 20:
            break
    if nbre in nombres:
        nombres.remove(nbre)
        if len(nombres) == 0:
            print(f'{nom_joueurs[nj]} est le joueur le plus chanceux')
    nj = (nj + 1) % 2
