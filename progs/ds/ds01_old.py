from random import randint

print(r""" ____  _     ____  ____  _     _____   _____ ____  _      _____
/  __\/ \ /\/_   \/_   \/ \   /  __/  /  __//  _ \/ \__/|/  __/
|  \/|| | || /   / /   /| |   |  \    | |  _| / \|| |\/|||  \  
|  __/| \_/|/   /_/   /_| |_/\|  /_   | |_//| |-||| |  |||  /_ 
\_/   \____/\____/\____/\____/\____\  \____\\_/ \|\_/  \|\____\
                                                               """)

puz_ab = 0
puz_ha = 0

while True:
    print()
    print("-- Tour de Hala")
    print("-" * 30)
    while True:
        choix_ha = input("Votre choix (P=Pair/I=Impair) ? ")
        if choix_ha == "P" or choix_ha == "I":
            break

    de = randint(1, 6)
    print("Dé =", de)

    if (puz_ha < 6) and ((choix_ha == "P" and de % 2 == 0) or (choix_ha == 'I' and de % 2 == 1)):
        puz_ha += 1
        print("Puzzle de Hala contient", puz_ha, "pièces")
    elif (puz_ab < 6):
        puz_ab += 1
        print("Puzzle de Abdou contient", puz_ab, "pièces")
    print()

    print()
    print("-- Tour de Abdou")
    print("-" * 30)
    while True:
        choix_ab = input("Votre choix (P=Pair/I=Impair) ? ")
        if choix_ab == "P" or choix_ab == "I":
            break

    de = randint(1, 6)
    print("Dé =", de)

    if (puz_ab < 6) and ((choix_ab == "P" and de % 2 == 0) or (choix_ab == 'I' and de % 2 == 1)):
        puz_ab += 1
        print("Puzzle de Abdou contient", puz_ab, "pièces")
    elif (puz_ha < 6):
        puz_ha += 1
        print("Puzzle de Hala contient", puz_ha, "pièces")
    print()

    if (puz_ha == 6) or (puz_ab == 6):
        break

if puz_ab == 6 and puz_ha == 6:
    print("Abdou et Hala vous avez gagné")
elif puz_ab == 6:
    print("Abdou tu es le gagnant")
else:
    print("Hala tu es la gagnante")

print()
print(r""" _____                      _____                
|  __ \                    |  _  |               
| |  \/ __ _ _ __ ___   ___| | | |_   _____ _ __ 
| | __ / _` | '_ ` _ \ / _ \ | | \ \ / / _ \ '__|
| |_\ \ (_| | | | | | |  __| \_/ /\ V /  __/ |   
 \____/\__,_|_| |_| |_|\___|\___/  \_/ \___|_|   """)

