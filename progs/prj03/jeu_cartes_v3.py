from random import randint

# Afficher le nom du jeu
print('=-' * 30)
print('|', 'Jeu de Trèfles'.center(56), '|')
print('=-' * 30)

# Afficher le principe du jeu
print()
print('Principe du jeu')
print('=-' * 15)
print('- Au début, dix cartes trèfles sont déposées sur une table,'
      ' faces cachées.')
print('A tour de rôle :')
print('- tu sélectionne une carte parmi les cartes existantes.')
print("- L'ordinateur en sélectionne une autre.")
print("Celui qui a la carte avec la petite valeur est gagnant du tour. "
      "Il marque un point.")
print("Le gagnant est celui avec le plus grand score.")
print()

# Mélanger les cartes
cartes = [
    'Lass', 'Douce', 'Tris', 'Quattro', 'Chinqa',
    'Sdous', 'Sbou', 'Amira', 'Amir', 'Roi'
]
jeu = cartes.copy()
nbre_cartes = len(jeu)
for i in range(nbre_cartes // 2):
    autre = randint(i+1, nbre_cartes - 1)
    jeu[i], jeu[autre] = jeu[autre], jeu[i]

score_ut = 0
score_or = 0
for partie in range(5):
    # Le joueur tire une carte
    nbre_cartes = len(jeu)
    print()
    print(f'Il reste {nbre_cartes} cartes.')

    print()
    print('>' * 5, 'Joueur'.center(12), '<' * 5)
    while True:
        nc = int(input(f'Numéro carte à tirer [1, {nbre_cartes}] ? '))
        if 1 <= nc <= nbre_cartes:
            break
        print(f'Erreur : Entrer un nombre [1, {nbre_cartes}]')

    carte_ut = jeu[nc - 1]
    print(f'Vous avez tiré : "{carte_ut}"')

    del jeu[nc - 1]

    # L'ordinateur tire une autre carte
    nbre_cartes = len(jeu)
    print()
    print(f'Il reste {nbre_cartes} cartes.')

    print()
    print('>' * 5, 'Ordinateur'.center(12), '<' * 5)
    nc = randint(0, nbre_cartes - 1)

    carte_or = jeu[nc]
    print(f'Je tire : "{carte_or}"')

    del jeu[nc]

    # Déterminer le gagnant du tour
    vc_ut = cartes.index(carte_ut)
    vc_or = cartes.index(carte_or)
    if vc_ut < vc_or:
        print(f'++ "{carte_ut}" bat "{carte_or}" => Tu as gagné')
        score_ut += 1
    else:
        print(f'-- "{carte_ut}" est battu par "{carte_or}" => Tu as perdu')
        score_or += 1

# Afficher le gagnant de la partie
print()
print(f'Score final : {score_ut} contre {score_or}')
if score_ut > score_or:
    print(f'Tu as gagné')
else:
    print(f'Tu as perdu')
