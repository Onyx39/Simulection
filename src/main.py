"""
Fichier principal, executable
"""

import matplotlib.pyplot as plt
import seaborn as sns

from classes.personnes.candidat import Candidat
from classes.personnes.electeur import Electeur
from classes.scrutins.uninominal_deux_tours import ScrutinUninominalDeuxTours

NOMBRE_CANDIDATS = 6
NOMBRE_ELECTEURS = 200

liste_electeurs = []
distribution_elecorat = []
for i in range (NOMBRE_ELECTEURS) :
    nouvel_electeur = Electeur(str(i))
    liste_electeurs.append(nouvel_electeur)
    distribution_elecorat.append(nouvel_electeur.positionnement)

liste_candidats = []
for i in range (NOMBRE_CANDIDATS) :
    nouveau_candidat = Candidat(str(i))
    liste_candidats.append(nouveau_candidat)
liste_candidats.sort()

for candidat in liste_candidats :
    print(candidat)

print(len(liste_candidats), len(liste_electeurs))
print(distribution_elecorat)

sns.displot(distribution_elecorat, kde=True, bins=20)
plt.savefig("resultats/distribution_electorat.png")

scrutin = ScrutinUninominalDeuxTours(liste_candidats, liste_electeurs)
scrutin.simulation_premier_tour()
