#ex7
from abc import ABC, abstractmethod

class Vehicule(ABC):
    @abstractmethod
    def deplacer(self):
        """Méthode abstraite pour déplacer le véhicule."""
        pass


class Voiture(Vehicule):
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele

    def deplacer(self):
        """Implémentation de la méthode deplacer pour une voiture."""
        return f"La voiture {self.marque} {self.modele} roule sur la route."


class Bicyclette(Vehicule):
    def __init__(self, marque, type_bicyclette):
        self.marque = marque
        self.type_bicyclette = type_bicyclette

    def deplacer(self):
        """Implémentation de la méthode deplacer pour une bicyclette."""
        return f"La bicyclette {self.marque} de type {self.type_bicyclette} avance sur le chemin."


# Exemple d'utilisation
voiture = Voiture("Toyota", "Corolla")
bicyclette = Bicyclette("Giant", "VTT")

print(voiture.deplacer())  # Affiche le déplacement de la voiture
print(bicyclette.deplacer())  # Affiche le déplacement de la bicyclette