#ex6
class Produit:
    def _init_(self, nom, prix):
        self.__nom = nom  # Attribut privé pour le nom
        self.__prix = prix  # Attribut privé pour le prix

    def get_nom(self):
        """Retourne le nom du produit."""
        return self.__nom

    def get_prix(self):
        """Retourne le prix du produit."""
        return self.__prix


class Commande:
    def _init_(self, produit, quantite):
        self.produit = produit  # Instance de Produit
        self.quantite = quantite  # Quantité de produit

    def calculer_total(self):
        """Calcule le total de la commande."""
        return self.produit.get_prix() * self.quantite


class Panier:
    def _init_(self):
        self.commandes = []  # Liste de commandes

    def ajouter_commande(self, commande):
        """Ajoute une commande au panier."""
        if isinstance(commande, Commande):
            self.commandes.append(commande)
        else:
            print("Erreur : L'objet ajouté n'est pas une commande.")

    def calculer_total_panier(self):
        """Calcule le total du panier."""
        total = sum(commande.calculer_total() for commande in self.commandes)
        return total


# Exemple d'utilisation
produit1 = Produit("Chaussures", 120)
produit2 = Produit("T-shirt", 30)

commande1 = Commande(produit1, 2)  # 2 paires de chaussures
commande2 = Commande(produit2, 3)  # 3 T-shirts

panier = Panier()
panier.ajouter_commande(commande1)
panier.ajouter_commande(commande2)

# Affichage du total du panier
total_panier = panier.calculer_total_panier()
print(f"Total du panier : {total_panier} dh")