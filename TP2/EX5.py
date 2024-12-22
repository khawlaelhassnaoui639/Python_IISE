
class Animal:
    def faire_du_bruit(self):
        print("l'animal fait du bruit")


class Chien(Animal):  
    def faire_du_bruit(self):
        print("le chien aboie :woof woof")


class Chat(Animal):
      def faire_du_bruit(self):
        print("le chat miaule :miao miao")
#tester la classe chien:
chien=Chien()
chien.faire_du_bruit()
#tester la classe chien:
chat=Chat()
chat.faire_du_bruit()





