# main.py

from src.math_operations import add, subtract, multiply, divide
from src.string_operations import concatenate, to_uppercase

def main():
    """
    Fonction principale qui utilise les modules math_operations et string_operations.
    Elle effectue des opérations mathématiques et manipule des chaînes de caractères.
    """
    
    # Utilisation des fonctions mathématiques
    print("Addition : ", add(5, 3))  # Test de l'addition de 5 et 3
    print("Soustraction : ", subtract(10, 4))  # Test de la soustraction de 4 à 10
    print("Multiplication : ", multiply(7, 6))  # Test de la multiplication de 7 par 6
    print("Division : ", divide(20, 5))  # Test de la division de 20 par 5

    # Utilisation des fonctions sur les chaînes
    print("Concaténation : ", concatenate("Bonjour", " tout le monde"))  # Concaténation de deux chaînes
    print("Majuscules : ", to_uppercase("hello world"))  # Conversion de la chaîne en majuscules

# Appeler la fonction principale si ce script est exécuté directement
if __name__ == "__main__":
    main()
