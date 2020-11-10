from random import randint

articles = [
    'voiture téléguidée',
    'ballon en cuir',
    'petite voiture téléguidée',
    'ours en peluche',
    'trompette',
    'ballon gonflable',
    'friandise',
    'chewing-gum'
]

poids = [
    0,
    1,
    12,
    50,
    314,
    706,
    1256,
    1962,
    2826
]

prix = [
    50000,
    15000,
    10000,
    5000,
    500,
    200,
    50,
    50
]

PRIX_ESSAI = 1000
NBRE_ESSAIS = 100000
gains = {}
depenses = 0
for i in range(NBRE_ESSAIS):
    num = randint(0, 2826)
    idx = min(i for i in range(len(poids)) if num <= poids[i])
    if idx < len(articles):
        art = articles[idx]
        if art not in gains:
            gains[art] = 0
        gains[art] += 1
        depenses += prix[idx]

print(gains)
print(depenses)
print(NBRE_ESSAIS * PRIX_ESSAI)
print(round(depenses * 100 / (NBRE_ESSAIS * PRIX_ESSAI)))
