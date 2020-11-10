# coding: utf8
print('Bienvenue, cher utilisateur')
print("Aujourd'hui, je vais jouer avec vous au jeu devine mon nombre.")
print()
print('Principe du jeu')
print('=-' * 30)
print('Le principe du jeu est simple : ')
print("- Vous choisissez un nombre dans l'intervalle [1, 127].")
print("- Je vais le deviner en 8 essais max.")
print("- Vous devez indiquer si mon nombre proposé est supèrieur, "
      "inférieur ou égal au votre.")
print()
print("Attention! Notez le nombre pour ne pas l'oublier.")
print()

bor_inf = 1
bor_sup = 127
for i in range(7):
    mid = (bor_inf + bor_sup) // 2
    print()
    print(f'Mon essai n°{i+1}')
    print('*' * 20)
    print(f'Je propose : {mid}')
    print('Le nombre secret est-t-il :')
    print('- supérieur à mon nombre (tapez >)')
    print('- inférieur à mon nombre (tapez <)')
    print('- égal à mon nombre (tapez =)')

    while True:
        reponse = input("? ")
        if len(reponse) == 1 and reponse in '<>=':
            break
        print('Saisie incorrecte {reponse}')
        print('Les réponses valides sont : ')
        print('> : si le nombre est supérieur à mon nombre')
        print('< : si le nombre est inférieur à mon nombre')
        print('= : si le nombre est égal à mon nombre')

    if reponse == '>':
        bor_inf = mid + 1
    elif reponse == '<':
        bor_sup = mid - 1
    else:
        print()
        print(':D :) ' * 10)
        print(f"Hoorray! J'ai trouvé en {i+1} coups.")
        break
