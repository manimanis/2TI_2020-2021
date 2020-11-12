a = int(input('Donner a : '))
b = int(input('Donner b : '))

# méthode 1
for i in range(a, b+1):
    if i % 3 == 0:
        print(i)

# méthode 2
if a % 3 > 0:
    a = a + 3 - a % 3
for i in range(a, b+1, 3):
    print(i)

# méthode 3
sa = a // 3
sb = b // 3
for i in range(sa, sb+1):
    v = 3 * i
    if a <= v <= b:
        print(v)
