from random import randint
from turtle import *

age = int(input('Entrer votre age : '))
nom = input('Entrer votre nom : ')

x = randint(5, 10)

if x >= 8:
    color('green')
    for _ in range(4):
        forward(100)
        left(90)
else:
    color('red')
    for _ in range(3):
        forward(120)
        left(120)

mainloop()
