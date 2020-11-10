print("Quantité d'eau pompée")
print("==-" * 15)

t = int(input("Quel est le temps d'irrigation (mn) ? "))

tp1 = t
if t > 60:
    tp1 = 60

print(f"Temps de fonct. pompe 1 : {tp1} mn")
print(f"Temps de fonct. pompe 2 : {t} mn")

qe1 = tp1 * 100
qe2 = t * 80
qe = qe1 + qe2

print(f"La quantité d'eau pompée est : {qe1} + {qe2} = {qe} litres")
