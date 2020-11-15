while True:
    a = int(input("Donner a ? "))
    if a > 0:
        break
    print('Valeur incorrecte')

while True:
    b = int(input("Donner b ? "))
    if b > 0:
        break
    print('Valeur incorrecte')

s = a + b
print(a, "+", b, "=", s)
