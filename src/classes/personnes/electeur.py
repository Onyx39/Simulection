"""
Classe qui represente les electeurs
"""

import random as rd

from classes.personnes.candidat import Candidat

class Electeur :
    """
    Classe electeur

    Entrée :
        nom (str) : nom de l'electeur

    Possede :
        positionnement (int [0, 100]) : positionnement politique
        candidat_favori (Candidat) : candidat favori    
    """

    def __init__ (self, nom : str) :
        self.nom = nom
        self.positionnement = rd.randint(0, 100)
        self.candidat_favori = None

    def __str__ (self) :
        return f"Electeur {self.nom} ({self.positionnement})"

    def assigner_candidat_favori (self, candidat : Candidat) :
        """"
        Assigne un candidat favor à un électeur

        Entrée :
            candidat (Candidat) : le candidat favori de l'électeur
        """
        self.candidat_favori = candidat

    def get_candidat_favori (self) :
        """"
        Renvoie le candidat favori de l'électeur
        """
        return self.candidat_favori
