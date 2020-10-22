print("Gestion de liste d'achats")

while True:
    n = int(input("Nombre d'articles : "))
    if n > 0:
        break
    print("Erreur : Vous allez acheter au moins un article")


qte_art = [0 for _ in range(n)]
articles = ["" for _ in range(n)]
print()
print("Saisie des articles")
print('=-' * 15)

for i in range(n):
    print()
    print(f"-- Article {i+1}")
    while True:
        art = input("Désignation ? ")
        art = art.strip().lower()
        if len(art) == 0:
            print("Erreur : Taper la désignation de l'article")
        elif art in articles:
            print("Erreur : Cet article est déjà saisi")
        else:
            articles[i] = art
            break
    while True:
        qte = float(input(f"Quantité de '{articles[i]}' ? "))
        if qte > 0.0:
            qte_art[i] = qte
            break
        print("Erreur : la quantité doit être strictement positive")

print()
print("Liste d'achats")
print("=-" * 15)
for i in range(n):
    print(f"{qte_art[i]:6.2f} {articles[i]}")