from random import randint


def saisie():
    return randint(10, 20)


def remplir(t, n):
    for i in range(n):
        t.append(randint(10, 99))


def saisiek(t):
    while True:
        k = randint(10, 99)
        if k not in t:
            return k


def deplacer(t, n, k):
    i = 0
    d = n-1
    while i < d:
        if t[i] < k:
            i += 1
        else:
            if t[d] < k:
                t[i], t[d] = t[d], t[i]
            else:
                d -= 1


def deplacer2(t, n, k):
    i, j = 0, n - 1
    while j > i:
        while i < j and t[i] < k:
            i += 1
        while i < j and t[j] > k:
            j -= 1
        if j > i:
            t[i], t[j] = t[j], t[i]
    return i


def afficher(t, n):
    for i in range(n):
        print(t[i], end=', ')
    print()


t = []
n = 0
k = 0
n = saisie()
remplir(t, n)
afficher(t, n)
k = saisiek(t)
print('k =', k)
idx = deplacer2(t, n, k)
t = t[:idx] + [k] + t[idx:]
n += 1
afficher(t, n)
