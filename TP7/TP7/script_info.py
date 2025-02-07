# script_info.py

import os
from datetime import datetime #pour manipuler les donnees lieer aux dates et heures
import math

def afficher_informations():
    # 1. Afficher le répertoire courant
    current_directory = os.getcwd() #répértoire courant
    print(f"Répertoire courant : {current_directory}")
    
    # 2. Afficher la date et l'heure actuelles
    now = datetime.now()
    print(f"Date et heure actuelles : {now.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 3. Calculer la racine carrée d'un nombre donné par l'utilisateur
    try:
        nombre = float(input("Entrez un nombre pour calculer sa racine carrée : "))
        if nombre < 0:
            print("Erreur : La racine carrée d'un nombre négatif n'est pas définie en réel.")
        else:
            racine = math.sqrt(nombre)
            print(f"La racine carrée de {nombre} est {racine}.")
    except ValueError:
        print("Erreur : Veuillez entrer un nombre valide.")

# Appeler la fonction principale
if __name__ == "__main__":
    afficher_informations()
