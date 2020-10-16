hd = int(input('Quelle est l\'heure de départ (hh:00) ? '))
hf = int(input('Quelle est l\'heure de fin (hh:00) ? '))
dt = int(input('Quelle est la durée du trajet ? '))

nv = (hf - hd) * 60 // dt

print(f'Le bus fait {nv} voyages de {hd}h à {hf}h.')