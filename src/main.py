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

liste_electeurs = []
distribution_elecorat = []
for i in range (NOMBRE_ELECTEURS) :
    nouvel_electeur = Electeur(str(i))
    liste_electeurs.append(nouvel_electeur)
    distribution_elecorat.append(nouvel_electeur.positionnement)

liste_candidats = []
distribution_candidats = []
for i in range (NOMBRE_CANDIDATS) :
    nouveau_candidat = Candidat(str(i))
    liste_candidats.append(nouveau_candidat)
    distribution_candidats.append(nouveau_candidat.positionnement)
liste_candidats.sort()
distribution_candidats.sort()

print(len(liste_candidats), len(liste_electeurs))
# print(liste_candidats)
# print(liste_electeurs)
print(distribution_candidats)
print(distribution_elecorat)

sns.displot(distribution_candidats, kde=True, bins=20)
plt.savefig("resultats/distribution_candidats.png")
sns.displot(distribution_elecorat, kde=True, bins=20)
plt.savefig("resultats/distribution_electorat.png")

votes = [0]*NOMBRE_CANDIDATS

def vote (votant : Electeur, candidats : list) -> int :
    """
    Simule le vote d'un électeur

    Entrées :
        votant (Electeur) : l'électeur votant
        candidats (list[Candidats]) : liste des candidats

    Retour :
        indice_votant (int) : indice du candadat pour lequel l'électeur vote dans la liste
    """
    min_distance = 100
    indice_votant = None
    egalite = 0
    for candidat in enumerate(candidats) :
        distance = abs(candidat[1].positionnement - votant.positionnement)
        if distance <  min_distance :
            min_distance = distance
            indice_votant = candidat[0]
            votant.assigner_candidat_favori(candidat[1])
        if distance ==  min_distance :
            egalite += 1
    print("Egalite : " + str(egalite))
    print(votant, votant.get_candidat_favori())
    return indice_votant

for electeur in liste_electeurs :
    vote_electeur = vote(electeur, liste_candidats)
    votes[vote_electeur] = votes[vote_electeur] + 1

print(votes, sum(votes))
plt.clf()
plt.cla()
plt.close()
sns.displot(distribution_candidats, kde=True, bins=20)
plt.savefig("resultats/distribution_candidats.png")
plt.plot(distribution_candidats, [x / NOMBRE_ELECTEURS for x in votes], "go")
plt.savefig("resultats/votes.png")
