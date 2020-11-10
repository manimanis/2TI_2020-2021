print("Temps de téléchargement")
print("==-"*15)

print("Nom des fichiers")
f1 = input("Fichier 1 ? ")
f2 = input("Fichier 2 ? ")

print("\nTaille des fichiers (Mo)")
tf1 = int(input(f"{f1} ? "))
tf2 = int(input(f"{f2} ? "))

print("\nVitesses de téléchargement (Mo/s)")
vt1 = float(input(f"{f1} ? "))
vt2 = float(input(f"{f2} ? "))

tt1 = int(tf1 / vt1)
tt2 = int(tf2 / vt2)

print("\nTemps de téléchargement")
print(f"{f1} : {tt1 // 3600}h {(tt1 // 60) % 60}mn {tt1%60}s")
print(f"{f2} : {tt2 // 3600}h {(tt2 // 60) % 60}mn {tt2%60}s")

print()
if tt1 < tt2:
    print(f"{f1} termine en premier")
elif tt1 > tt2:
    print(f"{f2} termine en premier")
else:
    print("Les deux fichiers terminent en même temps")
