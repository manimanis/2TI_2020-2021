from random import randint
from itertools import combinations

cartes = [
    'As',
    'Douce',
    'Tris',
    'Quatro',
    'Chinqa',
    'Sdous',
    'Sabaa',
    'Mojira',
    'Wezir',
    'Roi'
]

types = [
    'Carreau',
    'Trefle',
    'Coeur',
    'Spade'
]


# reconstituer les cartes
def reconstituer_cartes():
    jeu_cartes = []
    for nt in range(4):
        for nc in range(10):
            jeu_cartes.append((cartes[nc], types[nt]))
    return jeu_cartes


# melanger cartes
def melanger_cartes(jeu_cartes):
    jeu_cartes1 = []
    for _ in range(40):
        num = randint(0, len(jeu_cartes) - 1)
        jeu_cartes1.append(jeu_cartes[num])
        del jeu_cartes[num]
    return jeu_cartes1


# Afficher les cartes d'un joueur
def afficher_tachkila(msg, cartes):
    print(msg, ", ".join(f'{carte} {tc}' for carte, tc in cartes))


# Valeurs possibles
def combinaisons_cartes(table):
    possible = {}
    for i in range(1, len(table)):
        for cmb in combinations(table, i):
            s = sum(cartes.index(item[0])+1 for item in cmb)
            if s > 10: 
                continue
            if s not in possible:
                possible[s] = []
            possible[s].append(cmb)
    return possible


# Valeurs cartes
def valeurs_cartes(kef):
    valeurs = {}
    for i in range(len(kef)):
        item = kef[i]
        valeur = cartes.index(item[0])+1
        if valeur not in valeurs:
            valeurs[valeur] = []
        valeurs[valeur] = item
    return valeurs


# mettre 4 cartes sur la table
jeu_cartes = melanger_cartes(reconstituer_cartes())
table = jeu_cartes[:4]
jeu_cartes = jeu_cartes[4:]

while len(jeu_cartes) > 0:
    print('Distribution')
    ko = jeu_cartes[:3]
    kj = jeu_cartes[3:6]
    jeu_cartes = jeu_cartes[6:]
    for i in range(3):
        print(f'Tour n° {i+1}')
        afficher_tachkila('Table : ', table)
        afficher_tachkila('Ordinateur : ', ko)
        afficher_tachkila('Joueur : ', kj)
        comb_table = combinaisons_cartes(table)
        vals_ko = valeurs_cartes(ko)
        vals_kj = valeurs_cartes(kj)

        vko = set(vals_ko.keys())
        vtab = set(comb_table.keys())

        print('Ordinateur', '-' * 20)
        cposs = vko.intersection(vtab)
        mx = None
        for cas in cposs:
            cmb = comb_table[cas]
            if mx is None:
                mx = cmb[0]
            for item in cmb:
                if len(item) > len(mx):
                    mx = item
        if mx is None:
            num = randint(0, len(ko)-1)
            print('Ordinateur jette : ', ko[num])
            table.append(ko[num])
            del ko[num]
        else:
            s = sum(cartes.index(item[0])+1 for item in mx)
            print('Ordinateur joue : ', vals_ko[s])
            print('Ordinateur gagne : ', mx)
            for item in mx:
                table.remove(item)
            ko.remove(vals_ko[s])

        print('Joueur', '-' * 20)
        comb_table = combinaisons_cartes(table)
        vkj = set(vals_kj.keys())
        vtab = set(comb_table.keys())
        cposs = vkj.intersection(vtab)
        mx = None
        for cas in cposs:
            cmb = comb_table[cas]
            if mx is None:
                mx = cmb[0]
            for item in cmb:
                if len(item) > len(mx):
                    mx = item
        if mx is None:
            num = randint(0, len(kj)-1)
            print('Joueur jette : ', kj[num])
            table.append(kj[num])
            del kj[num]
        else:
            s = sum(cartes.index(item[0])+1 for item in mx)
            print('Joueur joue : ', vals_kj[s])
            print('Joueur gagne : ', mx)
            for item in mx:
                table.remove(item)
            kj.remove(vals_kj[s])

afficher_tachkila('Table : ', table)
