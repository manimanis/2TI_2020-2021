h = int(input('Donner la hauteur du triangle ? '))
for i in range(h):
    print(' ' * (h-i-1) + '*' * (2*i+1))
