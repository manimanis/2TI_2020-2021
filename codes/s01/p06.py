from turtle import *

long = int(input('Longueur : '))
nc = int(input('Nombre de cotés : '))
cbord = input('Couleur de bordure : ')
cremp = input('Couleur de remplissage : ')

color(cbord, cremp)
begin_fill()
for _ in range(nc):
    forward(long)
    left(360 / nc)
end_fill()
mainloop()
