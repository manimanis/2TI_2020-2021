# Nombre de cakes
while True:
    nbc = int(input('Entrer le nombre de cakes (> 0) ? '))
    if nbc > 0:
        break
    print('Erreur : Le nombre de cakes doit être supérieur à 0.')
    print()

# Taille du four
while True:
    tf = int(input('Entrer la taille du four (> 0) ? '))
    if tf > 0:
        break
    print('Erreur : La taille du four doit être supèrieure à 0.')
    print()

print(f'Nous allons cuir {nbc} cakes dans un four de {tf} places.')
print()

# Nombre de cuissons
nb_cuissons = nbc // tf + int(nbc % tf != 0)
print("- Ouvrir le four. Sortir le plateau.")
for i in range(1, nb_cuissons + 1):
    if nbc > tf:
        nc = tf
    else:
        nc = nbc

    nbc = nbc - nc
    print("Cuisson n°", i)
    print("- Mettre", nc, "cakes dans le plateau")
    print("- Remettre le plateau dans le four. Fermer le four.")
    print("- Attendre la cuisson")
    print("- Ouvrir le four. Sortir le plateau.")
    print("- Enlever les", nc, "cakes cuits")
    print()

print("- Remettre le plateau dans le four. Fermer le four.")
