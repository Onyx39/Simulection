"""
Scrutin uninominal à deux tours
"""

import matplotlib.pyplot as plt
import seaborn as sns

from classes.personnes.candidat import Candidat
from classes.personnes.electeur import Electeur

class ScrutinUninominalDeuxTours :
    """
    Classe qui présente une élection avec un scrutin uninominal à deux tours

    Entrées :
        liste_candidats (list[Candidat]) : la liste des candidats
        liste_electeurs (list[Electeurs]) : la liste des electeurs

    Possède :
        premier_qualifie (Candidat) : le premier candidat qualifié après le premier tour
        second_qualifie (Candidat) : le deuxième candidat qualifié après le premier tour
        vainqueur (Candidat) : le candidat vainqueur de l'élection
    """

    def __init__ (self, liste_candidats : list[Candidat], liste_electeurs : list[Electeur]) :
        self.candidats : list[Candidat] = liste_candidats
        self.electeurs : list[Electeur] = liste_electeurs
        self.premier_qualifie : Candidat = None
        self.second_qualife : Candidat = None
        self.vainqueur : Candidat = None

    def simulation_premier_tour (self) -> None :
        """
        Simule le premier tour de l'élection.
        Met à jour les variables 'premier_qualifie' et 'second_qualifié'
        """
        votes = [0]*len(self.candidats)
        distribution_candidats = []
        for candidat in self.candidats :
            distribution_candidats.append(candidat.positionnement)
        distribution_candidats.sort()

        for electeur in self.electeurs :
            vote_electeur = None
            min_distance = 100
            egalite = 0
            for candidat in enumerate(self.candidats) :
                distance = abs(candidat[1].positionnement - electeur.positionnement)
                if distance <  min_distance :
                    min_distance = distance
                    vote_electeur = candidat[0]
                    electeur.assigner_candidat_favori(candidat[1])
                if distance ==  min_distance :
                    egalite += 1
                    # print("Egalite : " + str(egalite))
            votes[vote_electeur] = votes[vote_electeur] + 1
        print(votes, sum(votes))
        plt.clf()
        plt.cla()
        plt.close()
        sns.displot(distribution_candidats, kde=True, bins=20)
        plt.savefig("resultats/distribution_candidats.png")
        plt.plot(distribution_candidats, [x / len(self.electeurs) for x in votes], "go")
        plt.savefig("resultats/votes.png")

        self.premier_qualifie = self.candidats[votes.index(max(votes))]
        votes_bis = votes.copy() # .remove(max(votes))
        print(votes, votes_bis)
        votes_bis.remove(max(votes))
        print(votes_bis)
        self.second_qualife = self.candidats[votes.index(max(votes_bis))]
        print(self.premier_qualifie, self.second_qualife)

    def simulation_deuxieme_tour (self) -> None :
        """
        Simule le deuxième tour de l'élection.
        Met à jour les variables 'premier_qualifie' et 'second_qualifié'
        """
        return True
