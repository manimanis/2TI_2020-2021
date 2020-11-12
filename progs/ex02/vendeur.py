print('Vendeur ambulant')
print('==-' * 15)

print("Indiquer le nombre d'articles de chaque catégorie :")
na = int(input("Catégorie A ? "))
nb = int(input("Catégorie B ? "))
nc = int(input("Catégorie C ? "))

ca = na * 0.5 + nb + nc * 2.0

print(f"Le chiffre d'affaires de la journée : {ca:0.3f} DT")
if ca < 35:
    print("Mauvais")
elif ca < 50:
    print("Bon")
else:
    print("Satisfaisant")
