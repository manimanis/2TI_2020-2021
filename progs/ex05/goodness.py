s = input("Donner une chaine de lettres majuscules ? ")
n = len(s)
while True:
    k = int(input(f"Donner le score de qualité à atteindre (0 ≤ k ≤ {n//2}) ? "))
    if 0 <= k <= n // 2:
        break

sq = 0
for i in range(n // 2):
    if s[i] != s[n - (i + 1)]:
        sq += 1

print(f"Le score de qualité de {s} est {sq}")

ncc = abs(sq - k)

print(f"Il faudra changer {ncc} caractères pour atteindre le score {k}.")
