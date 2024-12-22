
class Rectangle:
    def_init_(self,largeur,hauteur)
     self.largeur=largeur
     self.hauteur=hauteur
#methode pour calculer la surface:
   def calculer_surface(self):
    return self.hauteur * self.largeur
#methode pour calculer la surface:  
   def calculer_perimetre(self,largeur,hauteur):
    return 2(self.hauteur + self.largeur)

#création d'instance rectangle et affichage du surface et perimètre:
rectangle=Rectangle(20,30)
# Affichage de la surface et du périmètre
surface = rectangle.calculer_surface()
perimetre = rectangle.calculer_perimetre()

print(f"La surface du rectangle est {surface} m².")
print(f"Le périmètre du rectangle est  {perimetre} m.")


