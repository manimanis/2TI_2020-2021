from random import randint

# Générer la scoppa
cartes = [0] * 40
for i in range(40):
    cartes[i] = i % 10 + 1

# Mélanger les cartes
for i in range(20):
    nc = randint(20, 39)
    cartes[i], cartes[nc] = cartes[nc], cartes[i]

# Déposer 4 cartes sur la table
table = cartes[:4]
cartes = cartes[4:]

# Afficher les cartes sur la table
print("Les cartes sur la table")
print(*table)

# Donner 3 cartes au joueur
joueur = cartes[:3]
cartes = cartes[3:]

# Afficher les cartes du joueur
print("Les cartes du joueur")
print(*joueur)
