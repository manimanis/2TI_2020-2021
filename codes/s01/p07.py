from turtle import *

cote = int(input('Longueur coté : '))

if cote >= 100:
    color('red', 'green')
else:
    color('green', 'red')

begin_fill()
for _ in range(4):
    forward(cote)
    left(90)
end_fill()
mainloop()
