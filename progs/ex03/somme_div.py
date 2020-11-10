n = int(input('Donner un entier ? '))
sd = 0
for i in range(1, n+1):
    if n % i == 0:
        sd = sd + i
print('Somme des diviseurs :', sd)
