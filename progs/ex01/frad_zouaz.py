from random import randint
from time import sleep

print("Jeu Frad/Zouaz")
print('=-' * 20)
sleep(2)

print()
co = randint(0, 5)
cu = int(input("Votre choix [0, 5] ? "))
s = co + cu

sleep(1.5)

fz = int(input("0 : zouaz / 1 : frad ? "))

sleep(2)

print(f'{co} + {cu} = {s}')
if s % 2 == 0:
    print(f"{s} zouaz")
else:
    print(f"{s} frad")

if fz == s % 2:
    print('Tu as gagné!')
else:
    print('Haha! J\'ai gagné cette fois!')
