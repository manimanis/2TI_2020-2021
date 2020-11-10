from random import randint, seed

seed(62875)

for i in range(5):
    d = randint(10, 99)
    print('Pièce', i+1)
    print('Dimensions :', d)
    if d > 85:
        print('Bloquée')
        break
    elif d < 50:
        print('Trop petite. Rebus')
        continue
    print("Normale")

