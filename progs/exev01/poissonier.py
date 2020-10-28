print('Calcul du prix de vente')
print('==-'*15)

np = input("Quel est le nom du produit ? ")
pa = float(input("Quel est le prix d'achat (DT) ? "))

if 0 <= pa < 15:
    g = 0.2
elif pa < 30:
    g = 0.25
else:
    g = 0.35
print(f'Gain : {g * 100:.0f}%')

pv = pa * (1 + g)
print(f'Prix de vente : {pv:.3f} DT')
