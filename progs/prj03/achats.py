from random import randint

n = 10

prix_art = [0] * n
nom_art = [""] * n

for i in range(n):
    nom_art[i] = f"Article {i+1}"
    while True:
        prix = randint(1, 50) * 100
        if prix not in prix_art:
            break
    prix_art[i] = prix

print("Prix des articles")
print("=-" * 10)
for i in range(n):
    print(f"{nom_art[i]} : {prix_art[i]}")

argent = randint(1, 50) * 100

print()
print(f"Je dispose de {argent}")

pc = -1
for i in range(n):
    if (pc == -1 and prix_art[i] < argent) or (pc != -1 and prix_art[i] <= argent and (argent - prix_art[i]) < (argent - prix_art[pc])):
        pc = i

if pc == -1:
    print(f"Tu ne peux acheter aucun article avec {argent}")
else:
    print(f"L'article le plus cher que je peux acheter avec {argent} est {nom_art[pc]} et il coûte {prix_art[pc]}")

