#importation
import random


#Déclaration des classes et fonctions
class Jeu:
    """
    C'est un jeu
    """
    def __init__(self, m):
        """

        :param m: un nombre
        """
        self.k = random.randint(0, m)

#Programme principal
