n = int(input('Donner un entier ? '))
nd = 0
for i in range(1, n+1):
    if n % i == 0:
        nd = nd + 1
if nd == 2:
    print(n, "est premier")
else:
    print(n, "n'est pas premier")