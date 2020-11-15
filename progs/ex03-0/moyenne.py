while True:
    a = int(input("Donner a [1, 10] ? "))
    if 1 <= a <= 10:
        break
    print('Valeur incorrecte')

while True:
    b = int(input("Donner b [1, 10] ? "))
    if 1 <= b <= 10:
        break
    print('Valeur incorrecte')

m = (a + b) / 2
print("La moyenne de", a, "et", b, "est", m)
