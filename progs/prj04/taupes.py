from random import randint


def pseudo_valide(pseudo, pseudos):
    if len(pseudo) < 3:
        print('Erreur : le pseudo doit comporter au moins 3 caractères')
        return False
    if pseudo in pseudos:
        print('Erreur : le pseudo est déjà pris')
        return False
    return True


def saisir_pseudo(pseudos):
    while True:
        pseudo = input('Entrer votre pseudo ? ').strip().capitalize()
        if pseudo_valide(pseudo, pseudos):
            return pseudo


def remplir_pseudos():
    pseudos = ["" for i in range(2)]
    for i in range(2):
        print(f'Joueur {i+1} : ', end='')
        pseudos[i] = saisir_pseudo(pseudos)
    return pseudos


def init_trous():
    ntr = randint(4, 7) * 2
    trous = [0 for i in range(ntr)]
    nta = ntr // 2 + 1
    for i in range(nta):
        while True:
            p = randint(0, ntr-1)
            if trous[p] == 0:
                trous[p] = 1
                break
    return ntr, nta, trous


def afficher_trous(trous):
    ntr = len(trous)
    print()
    print(' Champs de carottes '.center(ntr * 6 + 1, '/'))
    print('+-----' * ntr + '+')
    print('|', end='')
    for i in range(ntr):
        ct = trous[i]
        if ct == 2:
            car = 'x'
        elif ct == 3:
            car = 'o'
        else:
            car = ''
        print(car.center(5), end='|')
    print('\n+', end='')
    for i in range(ntr):
        print(str(i).center(5, '-'), end='+')
    print('\n')


def taper(p, nc=1):
    score = 0
    for i in range(nc):
        ct = trous[p + i]
        if ct == 0:
            trous[p + i] = 3
        elif ct == 1:
            trous[p + i] = 2
            score += 1
    return score


def saisie_numero_trou(trous):
    ntr = len(trous)
    while True:
        num_tr = input("Numéro du trou ? ")
        if num_tr.isdigit():
            num_tr = int(num_tr)
            if 0 <= num_tr < ntr and trous[num_tr] in (0, 1):
                return num_tr
        print('Erreur : numéro de trou incorrect')


def afficher_scores(pseudos, scores):
    print()
    ml = max(len(pseudo) for pseudo in pseudos) + 4
    print('+' + 'Scores'.center(ml*2+3, '-') + '+')
    print('|' + f'{pseudos[0].center(ml, "-")}-+-{pseudos[1].center(ml, "-")}'
          + '|')
    print('|' + f'{str(scores[0]).center(ml)} | {str(scores[1]).center(ml)}'
          + '|')
    print('+' + '-' * (ml*2+3) + '+')
    print()


# Programme principal
print('+' + '-' * 50 + '+')
print('|' + 'Chasse aux taupes'.center(50) + '|')
print('+' + '-' * 50 + '+')
print()

pseudos = remplir_pseudos()
ntr, nta, trous = init_trous()
j = 0
nc = nta - 2
scores = [0 for _ in range(2)]
afficher_trous(trous)
for j in range(2):
    print()
    print(f'>>> Joueur n°{j+1} : {pseudos[j]}')
    print(f'Vous avez {nc} essais')
    for i in range(nc):
        print()
        print(f'- Essai n°{i+1}/{nc} --{pseudos[j]}--')
        num_tr = saisie_numero_trou(trous)
        taupe = taper(num_tr)
        scores[j] += taupe
        if taupe:
            print('=> Bravo! Vous avez assommé une taupe!')
        else:
            print('=> Trou vide!')
        afficher_scores(pseudos, scores)
        afficher_trous(trous)

print("Le jeu est terminé!")
afficher_scores(pseudos, scores)
if scores[0] == scores[1]:
    print('Match nul!')
elif scores[0] > scores[1]:
    print(f'{pseudos[0]} est vainqueur!')
else:
    print(f'{pseudos[1]} est vainqueur!')
