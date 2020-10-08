from random import randint

CHAMBRE_VIDE = ' '
CHAMBRE_TRESOR = 'T'
CHAMBRE_XRAYS = 'X'
CHAMBRE_ZOMBIE = 'Z'
CHAMBRE_ANTIDOTE = 'A'

# Nombre de chambres dans l'hôtel hanté
NBRE_CHAMBRES = 16
chambres = [CHAMBRE_VIDE for _ in range(NBRE_CHAMBRES)]


def placer_objets(chambres, objet, nbre):
    for _ in range(nbre):
        while True:
            num_ch = randint(0, NBRE_CHAMBRES - 1)
            if chambres[num_ch] == CHAMBRE_VIDE:
                chambres[num_ch] = objet
                break


def xrays_scan(chambres, num_ch):
    if chambres[num_ch] == CHAMBRE_VIDE:
        return 'vide'
    elif chambres[num_ch] == CHAMBRE_ANTIDOTE:
        return 'verre'
    elif chambres[num_ch] == CHAMBRE_TRESOR:
        return 'metal'
    elif chambres[num_ch] == CHAMBRE_XRAYS:
        return 'metal'
    elif chambres[num_ch] == CHAMBRE_ZOMBIE:
        return 'chaire et os'


# Sélectionner la chambre du trésor
placer_objets(chambres, CHAMBRE_TRESOR, 1)

# Sélectionner les chambres des pièges
placer_objets(chambres, CHAMBRE_ZOMBIE, 5)

# Sélectionner les chambres des rayons X
placer_objets(chambres, CHAMBRE_XRAYS, 5)

# Sélectionner les chambres des antidotes
placer_objets(chambres, CHAMBRE_ANTIDOTE, 2)

print(chambres)

print("Bienvenue dans l'hôtel hanté")
print(f"L'hotel comporte {NBRE_CHAMBRES} chambres,"
      f" numérotées de 0 à {NBRE_CHAMBRES - 1}, "
      "le trésor se trouve dans l'une d'entre elles.")
print("Trouve-le!")
print()
print("Attention! Certaines chambres contiennent des zombies."
      " Les méchants zombies peuvent te prendre des vies.")
print("D'autres chambres peuvent contenir un antidôte "
      "qui te donnera une vie supplémentaire.")
print("Allez-c'est parti!")
print()

vies = 3
while vies > 0:
    print(f'Vous avez {vies} vies')
    while True:
        choix = int(input("Quelle est le numéro de la chambre à visiter ? "))
        if 0 <= choix < NBRE_CHAMBRES:
            break
        print("Erreur : Sélectionner un nombre dans "
              f"l'intervalle [0, {NBRE_CHAMBRES - 1}]")
    if chambres[choix] == CHAMBRE_VIDE:
        print("Chambre vide, seulement quelques araignées l'habitent.")
    elif chambres[choix] == CHAMBRE_ANTIDOTE:
        print("Dans l'armoire apparait une bouteille d'antidôte.")
        print("Quelle chance vous gagner une nouvelle vie.")
        vies += 1
    elif chambres[choix] == CHAMBRE_TRESOR:
        print("Horrrray! Au fond de la chambre brille une caisse remplie d'or,"
              " de bijoux et de pierres précieuses, tu es devenu riche!")
        break
    elif chambres[choix] == CHAMBRE_XRAYS:
        print("Un détecteur à Rayon X est installé dans cette chambre.")
        print("Vous pouvez voir dans les deux chambres voisines")
        prec = (choix + NBRE_CHAMBRES - 1) % NBRE_CHAMBRES
        suiv = (choix + 1) % NBRE_CHAMBRES
        print(f"Chambre n°{prec} : {xrays_scan(chambres, prec)}")
        print(f"Chambre n°{suiv} : {xrays_scan(chambres, suiv)}")
    elif chambres[choix] == CHAMBRE_ZOMBIE:
        print("Un créature mort-vivant vous saute à la figure.")
        print("Vous perdez une vie!")
        vies -= 1
        if vies == 0:
            print("Vous êtes mort!")
            break
