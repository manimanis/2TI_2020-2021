from random import randint

NB_TOURS = 5

j1 = input('Nom du 1er joueur ? ')
j2 = input('Nom du 2nd joueur ? ')
joueurs = [j1, j2]

sj = [0, 0]
for tour in range(NB_TOURS):
    print('-' * 30)
    print('Tour n°', tour+1)

    nj = randint(0, 1)
    print('\nLe joueur', joueurs[nj], 'choisit')

    cj = int(input('0 : Pair / 1 : Impair ? '))

    cj1 = randint(0, 5)
    cj2 = randint(0, 5)
    print()
    print(j1, 'et', j2, 'tendent leurs mains')
    print(j1, ':',  cj1, '-', j2, ':',  cj2)

    s = cj1 + cj2

    if s % 2 == cj:
        njg = nj
        njp = (nj + 1) % 2
    else:
        njg = (nj + 1) % 2
        njp = nj
    sj[njg] += 1

    print(joueurs[njg], 'gagne ce tour.')
    print()

    if sj[njg] >= NB_TOURS // 2 + 1:
        break

if sj[0] > sj[1]:
    njg = 0
    njp = 1
else:
    njg = 1
    njp = 0
print(joueurs[njg], 'gagne la partie contre', joueurs[njp])
print('Score :', sj[njg], '-', sj[njp])
