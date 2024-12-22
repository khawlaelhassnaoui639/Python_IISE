
class Personne:
    def_init_(self,nom,prenom,age):
    self.nom=nom
    self.prenom=prenom
    self.age=age

    def se_presenter(self):
        #affichons une présentation de la personne:
    print(f"Bonjour, je m'appelle {self.prenom} {self.nom} et j'ai {self.age} ans.")

class Etudiant(Personne):
    def_init_(self,nom,prenom,age,matricule)
    #appeler le constructeur de la class mère "personne"
     super()._init_(nom,prenom,age)
     self.matricule=matricule

   def Etudier(self):
    print(f"{self.nom} {self.prenom} est entrain d'étudier")

    # Création d'un objet de type Personne
personne1 = Personne("khawla", "elhassnaoui", 20)
personne1.se_presenter()

# Création d'un objet de type Etudiant
etudiant1 = Etudiant("Khawla, "elhassnaoui", 20, "ETU12345")
etudiant1.se_presenter()
etudiant1.etudier()
