class Chien:
def_init(self,nom,race,age):
   self.nom=nom
   self.race=race
   self.age=age
     
   def aboyer(self):
    print("woof")

 #creation d'une instance de chien
    chien1=Chien(nom="Rex",race="haskie"age=3)
 #appel de la methode aboyer
     chien1.aboyer()
 

