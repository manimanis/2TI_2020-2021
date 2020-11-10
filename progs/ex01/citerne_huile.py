from math import pi

d = float(input('Donner le diamètre de la citerne (m) : '))
h = float(input('Donner l\'heuteur de la citerne (m) : '))
nh = float(input('Donner le niveau de l\'huile (%) : '))

vc = pi * d * d * h / 4
qh = int(vc * nh * 10)  # 10 = 1000 / 100

print(f'La citerne contient {qh} litres d\'huile.')
