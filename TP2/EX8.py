
# Classe Personne
class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.amis = []  # Liste pour stocker les amis

    def ajouter_ami(self, ami):
        # Ajoute un ami à la liste des amis
        if ami not in self.amis:  # Evite les doublons
            self.amis.append(ami)
        else:
            print(f"{ami.nom} est déjà dans la liste des amis de {self.prenom}.")

    def afficher_amis(self):
        # Affiche la liste des amis
        if not self.amis:
            print(f"{self.prenom} n'a pas d'amis.")
        else:
            print(f"Les amis de {self.prenom} {self.nom} :")
            for ami in self.amis:
                print(f"- {ami.prenom} {ami.nom}")


# Création de quelques personnes
personne1 = Personne(fatma", "boussaoula")
personne2 = Personne("khawla", "elhassnaoui")
personne3 = Personne("med", "alami")

# Ajout d'amis
personne1.ajouter_ami(personne2)
personne1.ajouter_ami(personne3)

# Tentative d'ajout d'un ami déjà existant
personne1.ajouter_ami(personne2)

# Affichage des amis
personne1.afficher_amis()
