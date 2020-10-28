from random import randint
from time import sleep

print("L'opérateur TN CELLS vous souhaite la bienvenue!")
t = float(input("Introduire le temps de rotation de la roulette ? "))
print("La roulette se met à tourner")
sleep(t)
print(f"Elle s'arrête au bout de {t} secondes")

ts = randint(1, 10)
if ts % 2 == 0:
    message = "Revenez la prochaine fois"
elif ts == 1:
    message = "Forfait Internet 500Mo"
elif ts == 3:
    message = "Forfait Internet 1Go"
elif ts == 5:
    message = "Forfait Internet 200Mo"
elif ts == 7:
    message = "Forfait Téléphonique 2h"
elif ts == 9:
    message = "Forfait Téléphonique 8h"

print(f"La roulette s'arrête devant le numéro {ts}")
print(message)
