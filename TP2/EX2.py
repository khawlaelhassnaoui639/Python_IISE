
class Voiture:
    def_init(self,marque,modèle,année):
   self.marque=marque
   self.modèle=modèle
   self.année=année

   def afficher_info(self):
    printf("marque ",self.marque,"modéle ",self.modèle,"année ",self.année)
     
     voiture1=Voiture(marque="toyota",modèle="MODEl03",année=2019)
     voiture2=Voiture(marque="dacia",modèle="MODEl02",année=2023)
     voiture3=Voiture(marque="BM",modèle="MODEl03",année=2020)

     voiture1.afficher_info()
     voiture2.afficher_info()
     voiture3.afficher_info()
    
          
     
