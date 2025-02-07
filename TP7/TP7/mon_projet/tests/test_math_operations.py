# tests/test_math_operations.py

import unittest
from src.math_operations import add, subtract, multiply, divide

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)  # Test de l'addition de 2 et 3
        self.assertEqual(add(-1, 1), 0)  # Test avec des nombres négatifs et positifs

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)  # Test de la soustraction de 3 à 5
        self.assertEqual(subtract(0, 5), -5)  # Test avec zéro et un nombre positif

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)  # Test de la multiplication de 4 par 3
        self.assertEqual(multiply(0, 3), 0)  # Test avec un facteur nul

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)  # Test de la division de 10 par 2
        # Test de la division par zéro (doit lever une exception)
        with self.assertRaises(ValueError):
            divide(10, 0)

# Exécution des tests
if __name__ == "__main__":
    unittest.main()
