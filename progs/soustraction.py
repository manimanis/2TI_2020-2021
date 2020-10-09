from random import randint

print('Jeu de soustraction')

nbre = randint(10, 99)
n1 = randint(1, nbre - 1)

print(f'{nbre} - {n1} = ?')
n2 = int(input())

if n2 == nbre - n1:
    print('Très bien!')
else:
    print('La bonne réponse est :')
    print(f'{nbre} - {n1} = {nbre - n1}')