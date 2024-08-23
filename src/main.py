"""
Fichier principal, executable
"""

import matplotlib.pyplot as plt
import seaborn as sns

from candidat import Candidat
from electeur import Electeur

NOMBRE_CANDIDATS = 6
NOMBRE_ELECTEURS = 200

# A = Candidat("A")
# print(A)

electeurs = []
distribution_elecorat = []
for i in range (NOMBRE_ELECTEURS) :
    nouvel_electeur = Electeur(str(i))
    electeurs.append(nouvel_electeur)
    distribution_elecorat.append(nouvel_electeur.positionnement)

candidats = []
distribution_candidats = []
for i in range (NOMBRE_CANDIDATS) :
    nouveau_candidat = Candidat(str(i))
    candidats.append(nouveau_candidat)
    distribution_candidats.append(nouveau_candidat.positionnement)
candidats.sort()
distribution_candidats.sort()

print(len(candidats), len(electeurs))
print(candidats)
print(electeurs)
print(distribution_candidats)
print(distribution_elecorat)


sns.displot(distribution_candidats, kde=True, bins=20)
plt.savefig("resultats/distribution_candidats.png")
sns.displot(distribution_elecorat, kde=True, bins=20)
plt.savefig("resultats/distribution_electorat.png")

votes = [0]*NOMBRE_CANDIDATS


def vote (electeur : Electeur, candidats : list) -> int :
    min_distance = 100
    indice_electeur = None
    egalite = 0
    for candidat in enumerate(candidats) :
        distance = abs(candidat[1].positionnement - electeur.positionnement)
        if distance <  min_distance :
            min_distance = distance
            indice_electeur = candidat[0]
        if distance ==  min_distance :
            egalite += 1
    print("Egalite : " + str(egalite))
    return indice_electeur

for electeur in electeurs :
    vote_electeur = vote(electeur, candidats)
    votes[vote_electeur] = votes[vote_electeur] + 1

print(votes, sum(votes))
plt.clf()
plt.cla()
plt.close()
sns.displot(distribution_candidats, kde=True, bins=20)
plt.savefig("resultats/distribution_candidats.png")
plt.plot(distribution_candidats, [x / NOMBRE_ELECTEURS for x in votes], "go")
plt.savefig("resultats/votes.png")