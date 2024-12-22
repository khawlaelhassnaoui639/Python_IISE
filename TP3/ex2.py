#ex2
class Personne:
    def __init__(self, nom, prenom, age):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age

    # Getter pour le nom
    def get_nom(self):
        return self.__nom

    # Setter pour le nom
    def set_nom(self, nom):
        if isinstance(nom, str) and nom.strip():
            self.__nom = nom.strip()
        else:
            raise ValueError("Le nom doit être une chaîne de caractères non vide.")

    # Getter pour le prénom
    def get_prenom(self):
        return self.__prenom

    # Setter pour le prénom
    def set_prenom(self, prenom):
        
            self.__prenom = prenom.strip()
    
        
    # Getter pour l'âge
    def get_age(self):
        return self.__age

    # Setter pour l'âge
    def set_age(self, age):
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            raise ValueError("L'âge doit être un entier positif.")

# Exemple d'utilisation

    personne = Personne("Boussaoula", "Fatma", 21)
    print("Nom:", personne.get_nom())
    print("Prénom:", personne.get_prenom())
    print("Âge:", personne.get_age())

    personne.set_nom("El-hassnaoui")
    personne.set_prenom("Khaoula")
    personne.set_age(22)

    print("Nom mis à jour:", personne.get_nom())
    print("Prénom mis à jour:", personne.get_prenom())
    print("Âge mis à jour:", personne.get_age())


