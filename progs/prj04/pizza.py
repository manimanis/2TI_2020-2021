pizzas = [
    'Margarita',
    'Régina',
    'Reine',
    'Napolitaine',
    'Végétarienne',
    'Calzone',
    'Quatre fromages',
    'Chevrette',
    'Romana',
    'Bambino'
]

comp_pizzas = [
    'Sauce tomate, fromage, origan',
    'Sauce tomate, fromage, jambon blanc, origan',
    'Sauce tomate, fromage, jambon blanc, champignon, origan',
    'Sauce tomate, fromage, anchois, olive, origan',
    'Sauce tomate, fromage, champignon, poivrons, pommes de terre, '
    'tomates fraiches, origan',
    'Sauce tomate, fromage, jambon blanc, champignon, oeuf, origan',
    'Sauce tomate, fromage, chèvre, bleu, mizotte, origan',
    'Sauce tomate, fromage, lardons, chèvre, oignons, origan',
    'Sauce tomate, fromage, poivrons, oignons, chorizo, oeuf, merguez, origan',
    'Sauce tomate, jambon, fromage'
]

prix_pizzas = [
    6.0,
    6.5,
    7.0,
    6.5,
    8.0,
    7.5,
    9.0,
    8.5,
    9.5,
    6.0
]


def afficher_pizzas():
    print()
    print('Nos Pizzas')
    print('=-=' * 20)
    for i in range(len(pizzas)):
        pizza = pizzas[i]
        composition = comp_pizzas[i]
        prix = prix_pizzas[i]

        print()
        print(f"{i+1}. {pizza} - Prix : {prix:0.3f}DT")
        print(composition)


def selectionner_pizza():
    while True:
        num_pizza = int(input(f"Numéro du pizza [1, {len(pizzas)}] ? "))
        if 1 <= num_pizza <= len(pizzas):
            return num_pizza - 1
        print(f'Erreur : Numéro du pizza [1, {len(pizzas)}]')


def selectionner_qte():
    while True:
        nb = int(input("Nombre de pizzas (0 pour annuler) ? "))
        if nb >= 0:
            return nb
        print("Erreur : donner une valeur positive, 0 pour annuler")


def afficher_commandes():
    print()
    print('Pizzas commandés')
    print('=-' * 20)
    total = 0.0
    if len(cmd_np) == 0:
        print('Aucune commande actuellement!')
    for i in range(len(cmd_np)):
        np = cmd_np[i]
        qte = cmd_qte[i]
        montant = prix_pizzas[np] * qte
        total += montant
        print()
        print(f'{i+1}. {pizzas[np]}')
        print(comp_pizzas[np])
        print(f'{qte} x {prix_pizzas[np]:0.3f} = {montant:0.3f}')
    print()
    print(f'Total : {total:0.3f} DT')


def ajouter_commande():
    afficher_pizzas()
    num_pizza = selectionner_pizza()
    qte = selectionner_qte()
    if qte > 0:
        cmd_np.append(num_pizza)
        cmd_qte.append(qte)


def selectionner_commande():
    while True:
        nc = int(input("Numéro de commande à supprimer (0 pour annuler) ? "))
        if 0 <= nc <= len(cmd_np):
            return nc
        print(f"Erreur : donner une valeur positive [1, {len(cmd_np)}]")


def supprimer_commande():
    if len(cmd_np) == 0:
        print('Aucune commande à supprimer')
        return
    afficher_commandes()
    nc = selectionner_commande()
    if nc == 0:
        return
    del cmd_np[nc-1]
    del cmd_qte[nc-1]


def menu_principal():
    print()
    print('Pizza royale')
    print("-" * 20)
    print('Bienvenue chez nous, vous allez déguster les meilleures pizzas')
    print()
    print('1. Afficher commandes')
    print('2. Ajouter une commande')
    print('3. Supprimer une commande')
    print('4. Confirmer la commande/Quitter')
    print()
    while True:
        choix = int(input("Votre choix [1, 4] ? "))
        if 1 <= choix <= 4:
            return choix
        print("Erreur: Entrer un nombre de 1 à 4")


def confirmer_commande():
    global cmd_np, cmd_qte
    if len(cmd_np) == 0:
        print()
        print('Aucune commande à confirmer')
        return

    afficher_commandes()
    print()
    while True:
        rep = input('Taper:\noui, pour commander\nnon, pour annuler : ')
        if rep.lower() in ('oui', 'non'):
            break
        print('Répondre par oui ou non')
    if rep == 'oui':
        print("Commande confirmée, elle est en cours de préparation.")
        print('Veuillez patienter un moment')
    else:
        print("Vos commandes ont été annulées!")
        print("Nous espérons vous voir prochainement!")
        print("A bientôt!")
        cmd_np = []
        cmd_qte = []


# PP
cmd_np = []
cmd_qte = []
while True:
    print()
    choix = menu_principal()
    if choix == 1:
        afficher_commandes()
    elif choix == 2:
        ajouter_commande()
    elif choix == 3:
        supprimer_commande()
    elif choix == 4:
        confirmer_commande()
        break

print()
print("Merci pour votre visite!")
