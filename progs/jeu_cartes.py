from random import randint

numeros = [
    'Lass', 'Douce', 'Tris', 'Quattro', 'Chinqa',
    'Sdous', 'Sbou', 'Amira', 'Amir', 'Roi'
]

print('=-' * 20)
print('|', 'Jeu de Trèfles'.center(36), '|')
print('=-' * 20)

print()
print('Principe du jeu')
print('=-' * 15)
print('- Au début, dix cartes trèfles sont déposées sur une table,'
      ' faces cachées.')
print('A tour de rôle :')
print('- tu sélectionne une carte parmi les cartes existantes.')
print("- L'ordintar en sélectionne une autre.")
print("Celui qui a la carte avec la petite valeur est gagnant du tour. "
      "Il marque un point.")
print("Le gagnant est celui avec le plus grand score.")
print()


# Construire les cartes
jeu = numeros.copy()

# Mélanger les cartes
nbre_cartes = len(jeu)
for i in range(nbre_cartes // 2):
    autre = randint(i+1, nbre_cartes - 1)
    jeu[i], jeu[autre] = jeu[autre], jeu[i]

score_ut = 0
score_or = 0
for partie in range(5):
    print()
    # Calculer le nombre de cartes restantes
    nbre_cartes = len(jeu)
    print(f'Il reste {nbre_cartes} cartes.')

    # Tirer une carte (utilisateur)
    print('>' * 5, 'Joueur', '<' * 5)
    while True:
        nc = int(input(f'Numéro carte à tirer [1, {nbre_cartes}] ? '))
        if 1 <= nc <= nbre_cartes:
            break
        print(f'Erreur : Entrer un nombre [1, {nbre_cartes}]')
    carte_ut = jeu[nc - 1]
    del jeu[nc - 1]
    print(f'Vous avez tiré : {carte_ut}')

    # Calculer le nombre de cartes restantes
    nbre_cartes = len(jeu)

    # Tirer une carte (ordinateur)
    print('>' * 5, 'Ordinateur', '<' * 5)
    nc = randint(0, nbre_cartes - 1)
    carte_or = jeu[nc]
    del jeu[nc]
    print(f'Je tire : {carte_or}')

    # Calculer qui gagne
    vc_ut = numeros.index(carte_ut)
    vc_or = numeros.index(carte_or)
    if vc_ut < vc_or:
        print(f'++ {carte_ut} bat {carte_or}')
        print('++ Tu as gagné')
        score_ut += 1
    else:
        print(f'-- {carte_ut} est battu par {carte_or}')
        print("-- Tu as perdu")
        score_or += 1

# Afficher score final
print()
print(f'Score final : {score_ut} contre {score_or}')
if score_ut > score_or:
    print(f'Tu as gagné')
else:
    print(f'Tu as perdu')
