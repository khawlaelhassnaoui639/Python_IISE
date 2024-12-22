#ex3
from math import pi

class Forme:
    def calculer_surface(self):
        raise NotImplementedError("Cette méthode doit être implémentée par les sous-classes")

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def calculer_surface(self):
        return self.largeur * self.hauteur

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def calculer_surface(self):
        return pi * (self.rayon ** 2)

def afficher_surface(formes):
    for forme in formes:
        print(f"La surface de {type(forme).__name__} est : {forme.calculer_surface()}")

