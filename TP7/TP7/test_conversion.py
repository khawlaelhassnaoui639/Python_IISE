import unittest
import conversion

class TestConversion(unittest.TestCase):

    def test_dollars_to_dirhams(self):
        # Test avec le taux par défaut (10)
        self.assertEqual(conversion.dollars_to_dirhams(100), 1000)
        # Test avec un taux personnalisé
        self.assertEqual(conversion.dollars_to_dirhams(100, taux_conversion=11), 1100)
        # Test avec 0 dollars
        self.assertEqual(conversion.dollars_to_dirhams(0), 0)
        # Test avec un montant négatif
        self.assertEqual(conversion.dollars_to_dirhams(-50), -500)

    def test_meters_to_kilometers(self):
        # Test avec une valeur standard
        self.assertEqual(conversion.meters_to_kilometers(1000), 1.0)
        # Test avec 0 mètres
        self.assertEqual(conversion.meters_to_kilometers(0), 0.0)
        # Test avec une grande distance
        self.assertEqual(conversion.meters_to_kilometers(5000), 5.0)
        # Test avec une valeur décimale
        self.assertAlmostEqual(conversion.meters_to_kilometers(1234), 1.234)

# Exécution des tests
if __name__ == "__main__":
    unittest.main()
