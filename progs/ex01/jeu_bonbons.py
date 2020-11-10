from random import randint
from time import sleep

print('Jeu de bonbons')
print('Vous lancez les dés pour gagner des bonbons! Miam!')

print('Lancement de dés')
sleep(1.5)

de1 = randint(1, 6)
de2 = randint(1, 6)
s = de1 + de2
print(f'Le nombre affiché est {de1} + {de2} = {s}')

if s == 2 or s == 12:
    print('Tu gagnes 2 bonbons')
elif s == 3 or s == 11:
    print('Tu gagnes un bonbon')
elif s == 4 or s == 10:
    print('Tu ne gagnes rien')
else:
    print('Tu perds un bonbon')
