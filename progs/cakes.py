# Nombre de cakes
nbc = 7
# Taille du four
tf = 4
# Nombre de cuissons
nb_cuissons = nbc // tf + int(nbc % tf != 0)
print("- Ouvrir le four. Sortir le plateau.")
for i in range(1, nb_cuissons + 1):
  if nbc > tf:
    nc = tf
  else:
    nc = nbc
  
  nbc = nbc - nc
  print("Cuisson n°", i)
  print("- Mettre", nc, "cakes dans le plateau")
  print("- Remettre le plateau dans le four. Fermer le four.")
  print("- Attendre la cuisson")
  print("- Ouvrir le four. Sortir le plateau.")
  print("- Enlever les", nc, "cakes cuits")

print("- Remettre le plateau dans le four. Fermer le four.")
