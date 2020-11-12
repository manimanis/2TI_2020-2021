from random import randint

print("Jeu de dès")
print("==-" * 10)

de1 = randint(1, 6)
de2 = randint(1, 6)
de3 = randint(1, 6)

if de1 == de2 == de3:
    gain = 300
elif de1 == de2 or de1 == de3 or de2 == de3:
    gain = 200
elif de1 == 6 or de2 == 6 or de3 == 6:
    gain = 100
elif de1 + de2 == 6 or de1 + de3 == 6 or de2 + de3 == 6:
    gain = 50
else:
    gain = de1 + de2 + de3

print(f"de1 : {de1} - de2 : {de2} - de3 : {de3}")
print(f"gain : {gain} points")
