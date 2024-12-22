#ex5
class Employe:
    def __init__(self, nom, prenom, salaire):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire

    def afficher_informations(self):

        return f"Nom: {self.nom}, Prénom: {self.prenom}, Salaire: {self.salaire} dh"


class Manager(Employe):
    def __init__(self, nom, prenom, salaire):
        super().__init__(nom, prenom, salaire)
        self.employes_supervises = []  # Liste des employés supervisés

    def ajouter_employe(self, employe):
        if isinstance(employe, Employe):
            self.employes_supervises.append(employe)
        else:
            print("Erreur : L'objet ajouté n'est pas un employé.")

    def afficher_employes_supervises(self):
        """Affiche la liste des employés supervisés par le manager."""
        if not self.employes_supervises:
            return "Aucun employé supervisé."
        
        informations = "Employés supervisés :\n"
        for employe in self.employes_supervises:
            informations += f"- {employe.afficher_informations()}\n"
        return informations


# Exemple d'utilisation
employe1 = Employe("Boussaoula", "fatma", 3000)
employe2 = Employe("El-hassnaoui", "Khawla", 2800)
manager = Manager("Assiri", "Hamdi", 5000)

# Ajout des employés au manager
manager.ajouter_employe(employe1)
manager.ajouter_employe(employe2)

# Affichage des informations du manager et des employés supervisés
print(manager.afficher_informations())
print(manager.afficher_employes_supervises())