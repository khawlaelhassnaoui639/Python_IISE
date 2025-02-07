# src/math_operations.py
#fonction pour la somme
def add(a, b):
    return a + b
#fonction pour la soustraction:
def subtract(a, b): 
    return a - b
#fonction pour la multiplication:
def multiply(a, b):
    return a * b
#fonction pour la division:
def divide(a, b):
    # Vérification de la division par zéro
    if b == 0:
        raise ValueError("impossible de déviser par zero")
    return a / b
