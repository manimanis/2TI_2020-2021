base = int(input('Donner la longueur de la base ? '))
for i in range(base):
    if i == 0 or i == base-1:
        print('*' * (i + 1))
    else:
        print('*' + ' ' * (i-1) + '*')
