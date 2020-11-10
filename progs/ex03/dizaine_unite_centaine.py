print('méthode 1')
for i in range(100, 1000):
    c = i // 100
    d = (i // 10) % 10
    u = i % 10
    if d == c + u:
        print(i)

print('méthode 2')
for i in range(10, 99):
    c = i // 10
    d = i % 10
    if d >= c:
        u = d - c
        v = c*100+d*10+u
        print(v)

print('méthode 3')
for c in range(1, 10):
    for d in range(c, 10):
        u = d - c
        v = c*100+d*10+u
        print(v)
