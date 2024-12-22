#ex4
class Produit:
    def __init__(self, nom, prix):
        self.__nom = nom  # Attribut privé pour le nom
        self.__prix = prix  # Attribut privé pour le prix

    def get_nom(self):
        
        return self.__nom

    def get_prix(self):
        return self.__prix

    def appliquer_remise(self, pourcentage_remise, seuil):
        if self.__prix > seuil:
            remise = (self.__prix * pourcentage_remise) / 100
            prix_apres_remise = self.__prix - remise
            return prix_apres_remise
        else:
            return self.__prix

# Exemple d'utilisation
produit = Produit("Chaussures", 120)
print(f"Nom du produit: {produit.get_nom()}")
print(f"Prix original: {produit.get_prix()} dh")
prix_final = produit.appliquer_remise(10, 100)  # 10% de remise si le prix > 100
print(f"Prix après remise: {prix_final} dh")