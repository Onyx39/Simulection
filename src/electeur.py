"""
Classe qui represente les electeurs
"""

import random as rd

class Electeur :
    """
    Classe electeur

    Entrée :
        nom (str) : nom de l'electeur

    Possede :
        positionnement (int [0, 100]) : positionnement politique    
    """

    def __init__ (self, nom : str) :
        self.nom = nom
        self.positionnement = rd.randint(0, 100)

    def __str__ (self) :
        return f"Electeur {self.nom} ({self.positionnement})"
