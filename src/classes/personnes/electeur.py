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
        tolerance (int [5, 80]) : toleance pour voter pour un·e candidat·e
        candidat_favori (Candidat) : candidat favori    
    """

    def __init__ (self, nom : str) :
        self.nom : str = nom
        self.positionnement : int = rd.randint(0, 100)
        self.tolerance : int = rd.randint(1, 100)
        self.candidat_favori  : Candidat = None

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
