from turtle import *
long = int(input('Longueur : '))
nc = int(input('Nombre de cotés : '))

color('blue', 'gold')

begin_fill()
for _ in range(nc):
    forward(long)
    left(360 / nc)
end_fill()

mainloop()
