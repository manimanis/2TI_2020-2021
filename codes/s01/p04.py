from turtle import *
long = int(input('Longueur : '))
nc = int(input('Nombre de cotés : '))
for _ in range(nc):
    forward(long)
    left(360 / nc)
mainloop()
