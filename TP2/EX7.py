
# Classe Livre
class Livre:
    def __init__(self, titre, auteur, annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication

    def __str__(self):
        return f"'{self.titre}' par {self.auteur} (Publié en {self.annee_publication})"

# Classe Bibliotheque
class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        # Ajoute un livre à la liste des livres de la bibliothèque
        self.livres.append(livre)

    def afficher_livres(self):
        # Affiche tous les livres de la bibliothèque
        if not self.livres:
            print("La bibliothèque est vide.")
        else:
            for livre in self.livres:
                print(livre)


# Création de quelques livres
livre1 = Livre("1984", "George Orwell", 1949)
livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943)

# Création d'une bibliothèque
bibliotheque = Bibliotheque()

# Ajout des livres à la bibliothèque
bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)

# Affichage des livres de la bibliothèque
bibliotheque.afficher_livres()
