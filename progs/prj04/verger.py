from random import randint, seed

print('+' + '-' * 40 + '+')
print('|' + "Jeu du verger".center(40) + '|')
print('+' + '-' * 40 + '+')
print()

arbres = ['poire', 'pomme', 'prune', 'cerise']
de = ['corbeau'] + arbres + ['panier']
plateforme = {
    'poire': 10,
    'pomme': 10,
    'prune': 10,
    'cerise': 10,
    'corbeau': 0
}


def lancer_de():
    return de[randint(0, 5)]


def ceuillir_fruit(fruit):
    if plateforme[fruit] > 0:
        print('Tu as cueilli une', fruit)
        plateforme[fruit] -= 1
    else:
        print(f"Tu ne pas cueillir une {fruit}, l'abre est vide.")


def construire_puzzle():
    if plateforme['corbeau'] < 9:
        print("Ajout d'une pièce au puzzle du corbeau")
        plateforme['corbeau'] += 1


def jeu_gagne():
    for i in range(len(arbres)):
        if plateforme[arbres[i]] != 0:
            return False
    return True


def jeu_perdu():
    return plateforme['corbeau'] == 9


def inventaire():
    print()
    print('Inventaire')
    print('-' * 20)
    for i in range(len(arbres)):
        arbre = arbres[i]
        if plateforme[arbre] > 0:
            print(f"Il y'a {plateforme[arbre]} {arbre}"
                  f"{'s' if plateforme[arbre] > 1 else ''} sur l'arbre.")
    print(f"Le puzzle du corbeau contient {plateforme['corbeau']} pièces "
          "sur 9")


def saisie_nb_joueurs():
    while True:
        try:
            nb = int(input("Quel est le nombre de joueurs [2, 8] ? "))
            if 2 <= nb <= 8:
                return nb
        except ValueError:
            pass
        print('Erreur : le nombre de joueur est compris entre 2 et 8')


def saisie_joueurs(nb):
    joueurs = []
    for i in range(nb):
        while True:
            joueur = input(f"Nom du joueur n° {i+1} ? ").capitalize().strip()
            if joueur != '':
                break
            print('Erreur : nom invalide')
        joueurs.append(joueur)
    return joueurs


def arbres_non_vides():
    choix = []
    for i in range(len(arbres)):
        if plateforme[arbres[i]] != 0:
            choix.append(i)
    return choix


def choix_fruit():
    print()
    print('Choix d\'un fruit')
    print('Les possibilités restantes')
    choix = arbres_non_vides()
    for i in range(len(choix)):
        arbre = arbres[choix[i]]
        print(f"{choix[i]+1}. {arbre} : {plateforme[arbre]}")
    while True:
        try:
            rep = int(input("Votre choix ? ")) - 1
            if rep in choix:
                return arbres[rep]
        except ValueError:
            pass
        print("Erreur : Sélectionner parmi les choix proposés")


def jouer_tour(joueur):
    print()
    print('- Tour de', joueur)
    input('Appuyer sur Entrée pour lancer le dé...')
    de = lancer_de()
    print(f'Le dé tombe sur la face "{de}"')
    if de in arbres:
        ceuillir_fruit(de)
    elif de == 'corbeau':
        construire_puzzle()
    else:
        fruit = choix_fruit()
        ceuillir_fruit(fruit)
        if not jeu_gagne():
            fruit = choix_fruit()
            ceuillir_fruit(fruit)


# Programme Principal
# seed(892012)  # test_verger.txt
# seed(2861975)  # test_verger1.txt
# seed(2481983)  # test_verger2.txt
nb = saisie_nb_joueurs()
joueurs = saisie_joueurs(nb)
nj = 0
tour = 0
while not (jeu_gagne() or jeu_perdu()):
    if nj == 0:
        tour += 1
        print()
        print(f'>>> Tour n°{tour}')
        print()
    jouer_tour(joueurs[nj])
    inventaire()
    # input("\nAppuyez sur Entrée pour continuer...")
    nj = (nj + 1) % len(joueurs)

print()
if jeu_gagne():
    print("Félicitations vous avez gagné.")
else:
    print("Le méchant corbeau a gagné le jeu, il a volé tous les fruits.")
