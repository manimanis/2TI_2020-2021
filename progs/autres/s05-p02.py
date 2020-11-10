print('League of Legends contest')
print('=-=' * 15)

# Phase d'inscription
# ------------------------------------------
print()
print('Inscription des joueurs')
print('=-' * 15)

# Saisir le nombre de joueurs
print()
while True:
    n = int(input("Nombre de joueurs ( > 3) : "))
    if n > 3:
        break
    print('Erreur : Le nombre de joueurs doit être supérieur à 3')

# Saisir les pseudos des joueurs
lplayers = ["" for _ in range(n)]
for i in range(n):
    while True:
        player = input(f'Player n°{i+1} - Pseudo (de 3 à 12 lettres) : ')
        player = player.strip().upper()
        if player.isalpha() and len(player) > 12:
            player = player[:12]
        if player in lplayers:
            print(f"Erreur : Le joueur {player} est déjà inscrit")
        elif len(player) < 3:
            print("Erreur : Le pseudo doit comporter au moins 3 lettres")
        else:
            break
    lplayers[i] = player

# Saisir les scores des joueurs
print()
print('Scores des joueurs')
print('=-' * 15)
lscores = [0 for _ in range(n)]
for i in range(n):
    while True:
        score = int(input(f'Score de "{lplayers[i]}" > 0 : '))
        if score > 0:
            break
        print('Erreur : le score doit être strictement positif')
    lscores[i] = score

# Supprimer les duplications du score
lscores_copie = list(set(lscores.copy()))
# Ordonner les scores en ordre décroissant
lscores_copie.sort(reverse=True)

prix = ['10000DT', '6000DT', '3000DT']

# Afficher le rang des joueurs
print()
print('Rang des joueurs')
print('=-' * 15)
for i in range(len(lscores_copie)):
    print(f'{i+1}. {lscores_copie[i]:5}', end=' : ')
    for j in range(n):
        if lscores[j] == lscores_copie[i]:
            print(lplayers[j], end=' / ')
    print()

# Afficher les titulaires des trois premiers prix
print()
print('Distribution des prix')
print('=-' * 15)
for i in range(min(len(lscores_copie), len(prix))):
    print(f'Titulaires du prix {prix[i]}', end=' : ')
    for j in range(n):
        if lscores[j] == lscores_copie[i]:
            print(lplayers[j], end=' / ')
    print()


