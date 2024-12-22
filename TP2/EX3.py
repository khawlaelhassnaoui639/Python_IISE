
class CompteBancaire:
    
def_init_(self,titulaire,solde):
  self.titulaire=titulaire
  self.solde=solde

def deposer(self,montant):
  if montant > 0:
     self.solde+=montant
    print("le solde deposer est:"+self.solde)
  else:       
     print("Le montant à déposer doit être positif.")


def retirer(self,montant):
  if montant > 0:
  self.solde-=montant
  print("le solde retirer est:"+self.solde)
  else:
    print("solde insuffusant pour effectuer un retrait")


def afficher_solde(self):
  print(f"Solde actuel du compte de {self.titulaire}: {self.solde}€")

#test 
#création d'un compte bancaire:
compte=CompteBancaire("Mohamed",1400§)

#deposer un montant:
compte.deposer(30)

#deposer un montant:
compte.retirer(50)

#deposer un montant:
compte.afficher_solde()









  


     
=======
def intersection(ensemble1, ensemble2):
    # Créer un nouvel ensemble pour stocker l'intersection
    resultat = set()
    
    # Parcourir chaque élément du premier ensemble
    for element in ensemble1:
        # Si l'élément est aussi dans le deuxième ensemble, on l'ajoute à l'intersection
        if element in ensemble2:
            resultat.add(element)
    
    return resultat
# Tests
print(intersection({1, 2, 3}, {2, 3, 4}))  # Devrait afficher {2, 3}
print(intersection({1, 5, 7}, {7, 8, 9}))  # Devrait afficher {7}
>>>>>>> cb1859d (Add README.md)
