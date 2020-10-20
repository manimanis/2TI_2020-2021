d1 = int(input("Distance maison Karim (km) ? "))
d2 = int(input("Distance maison Ahmed (km) ? "))
v1 = int(input("Vitesse voiture Karim (km/h) ? "))
v2 = int(input("Vitesse voiture Ahmed (km/h) ? "))

t1 = d1 * 60 // v1
t2 = d2 * 60 // v2

print(f"Karim arrive au café après {t1} minutes")
print(f"Ahmed arrive au café après {t2} minutes")

if t1 > t2:
    print("Toujours en retard Karim ?")
elif t1 < t2:
    print("Toujours en retard Ahmed ?")
else:
    print("Au bon moment!")
