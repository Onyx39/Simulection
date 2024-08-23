"""
Classe qui represente les candidats
"""

import random as rd

class Candidat :
    """
    Classe candidat

    Entrée :
        nom (str) : nom du candidat

    Possede :
        positionnement (int [0, 100]) : positionnement politique    
    """

    def __init__ (self, nom : str) :
        self.nom = nom
        self.positionnement = rd.randint(0, 100)
    
    def __lt__ (self, other) :
        if self.positionnement < other.positionnement :
            return True
        return False

    def __str__ (self) :
        return f" Candidat {self.nom} ({self.positionnement})"
