print("Quantité d'eau pompée")
print("==-" * 15)

t = int(input("Quel est le temps d'irrigation (mn) ? "))

tp1 = t
if t > 60:
    tp1 = 60
tp2 = t

print(f"Temps de fonct. pompe 1 : {tp1} mn")
print(f"Temps de fonct. pompe 2 : {t} mn")

dp1 = 100
dp2 = 80
qe1 = tp1 * dp1
qe2 = tp2 * dp2
qe = qe1 + qe2

print(f"La quantité d'eau pompée est : {qe1} + {qe2} = {qe} litres")
