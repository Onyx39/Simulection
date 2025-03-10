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
        vote_blanc (bool) : autorisation du vote blanc, par défaut à False

    Possède :
        premier_qualifie (Candidat) : le premier candidat qualifié après le premier tour
        second_qualifie (Candidat) : le deuxième candidat qualifié après le premier tour
        vainqueur (Candidat) : le candidat vainqueur de l'élection
    """

    def __init__ (self, liste_candidats : list[Candidat],
                  liste_electeurs : list[Electeur],
                  vote_blanc : bool = False) :
        self.candidats : list[Candidat] = liste_candidats
        self.electeurs : list[Electeur] = liste_electeurs
        self.vote_blanc : bool = vote_blanc
        self.premier_qualifie : Candidat = None
        self.second_qualife : Candidat = None
        self.vainqueur : Candidat = None


    def simulation_premier_tour (self) -> list[Candidat] :
        """
        Simule le premier tour de l'élection.
        Met à jour les variables 'premier_qualifie' et 'second_qualifié'

        Retourne la liste des deux candidat·e·s qualifié·e·s
        """
        votes : list[int] = [0]*len(self.candidats)
        if self.vote_blanc :
            votes.append(0)
        distribution_candidats : list[int] = []
        for candidat in self.candidats :
            distribution_candidats.append(candidat.positionnement)
        distribution_candidats.sort()

        for electeur in self.electeurs :
            vote_electeur : Candidat = None
            min_distance : int = 100
            # egalite = 0
            for candidat in enumerate(self.candidats) :
                distance : int = abs(candidat[1].positionnement - electeur.positionnement)
                if distance <  min_distance :
                    if self.vote_blanc and distance > electeur.tolerance :
                        # print("pas assez tolérant")
                        # votes[-1] = votes[-1] + 1
                        pass
                    else :
                        min_distance = distance
                        vote_electeur = candidat[0]
                        electeur.assigner_candidat_favori(candidat[1])
                # if distance ==  min_distance :
                #     egalite += 1
                    # print("Egalite : " + str(egalite))
            if vote_electeur is not None :
                votes[vote_electeur] = votes[vote_electeur] + 1
            else :
                votes[-1] = votes[-1] + 1
        print(votes, sum(votes))
        if self.vote_blanc :
            print("Nombre de votes blanc : ", votes[-1], " soit ",
                votes[-1]/len(self.electeurs), "% des électeurs")

        self.premier_qualifie = self.candidats[votes.index(max(votes))]
        votes_bis : list[int] = votes.copy()
        votes_bis.remove(max(votes))
        self.second_qualife = self.candidats[votes.index(max(votes_bis))]
        print(self.premier_qualifie, self.second_qualife)

        plt.clf()
        plt.cla()
        plt.close()
        sns.displot(distribution_candidats, kde=False, bins=100)
        plt.xlim(0, 100)
        plt.savefig("resultats/distribution_candidats.png")
        plt.clf()
        plt.cla()
        plt.close()
        if self.vote_blanc :
            plt.plot(distribution_candidats, [x / len(self.electeurs) for x in votes[:-1]], "go")
        else :
            plt.plot(distribution_candidats, [x / len(self.electeurs) for x in votes], "go")
        plt.savefig("resultats/votes_1er_tour.png")

        return [self.premier_qualifie, self.second_qualife]


    def simulation_deuxieme_tour (self) -> Candidat :
        """
        Simule le deuxième tour de l'élection.
        Met à jour les variables 'vainqueur'

        Retourne lea candidat·e vainqueur·e
        """

        votes : list[int] = [0, 0]
        distribution_candidats : list[int] = [self.premier_qualifie.positionnement,
                                              self.second_qualife.positionnement]
        distribution_candidats.sort()

        for electeur in self.electeurs :
            vote_electeur : Candidat = None
            min_distance : int = 100
            egalite : int = 0
            for candidat in enumerate([self.premier_qualifie, self.second_qualife]) :
                distance : int = abs(candidat[1].positionnement - electeur.positionnement)
                if distance <  min_distance :
                    min_distance = distance
                    vote_electeur = candidat[0]
                if distance ==  min_distance :
                    egalite += 1
                    # CAS EGALITE
                    # print("Egalite : " + str(egalite))
            votes[vote_electeur] = votes[vote_electeur] + 1
        print(votes, sum(votes))

        self.vainqueur = [self.premier_qualifie, self.second_qualife][votes.index(max(votes))]
        print(self.vainqueur)

        plt.clf()
        plt.cla()
        plt.close()
        plt.plot(distribution_candidats, [x / len(self.electeurs) for x in votes], "go")
        plt.savefig("resultats/votes_2eme_tour.png")

        return self.vainqueur


    def simulation_complete (self) :
        """
        Simulation des deux tours du scrutin
        """
        self.simulation_premier_tour()
        self.simulation_deuxieme_tour()
