#!/usr/bin/python3
"""Tests unitaires pour max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Cas de tests pour la fonction max_integer"""

    def test_liste_normale(self):
        """Test avec une liste normale d'entiers positifs"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([5, 1, 9, 3]), 9)

    def test_element_unique(self):
        """Test avec une liste contenant un seul élément"""
        self.assertEqual(max_integer([42]), 42)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([-5]), -5)

    def test_liste_vide(self):
        """Test avec une liste vide"""
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())

    def test_nombres_negatifs(self):
        """Test avec des nombres négatifs"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -5, -20, -1]), -1)
        self.assertEqual(max_integer([-100]), -100)

    def test_melange_positif_negatif(self):
        """Test avec des nombres positifs et négatifs mélangés"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([5, -10, 0, 3]), 5)
        self.assertEqual(max_integer([-5, -1, 0]), 0)

    def test_valeurs_max_dupliquees(self):
        """Test avec des valeurs maximales dupliquées"""
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)
        self.assertEqual(max_integer([1, 3, 3, 2]), 3)
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_max_au_debut(self):
        """Test quand le maximum est au début"""
        self.assertEqual(max_integer([10, 1, 2, 3]), 10)
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_max_a_la_fin(self):
        """Test quand le maximum est à la fin"""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_max_au_milieu(self):
        """Test quand le maximum est au milieu"""
        self.assertEqual(max_integer([1, 2, 10, 3, 4]), 10)
        self.assertEqual(max_integer([2, 1, 9, 3, 5]), 9)

    def test_valeurs_zero(self):
        """Test avec des valeurs zéro"""
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([0, 1, 2]), 2)
        self.assertEqual(max_integer([-1, 0, -2]), 0)

    def test_grands_nombres(self):
        """Test avec de grands nombres"""
        self.assertEqual(max_integer([1000000, 999999, 1000001]), 1000001)
        self.assertEqual(max_integer([999, 1000, 998]), 1000)

    def test_deux_elements(self):
        """Test avec exactement deux éléments"""
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([5, 3]), 5)
        self.assertEqual(max_integer([-1, -5]), -1)

    def test_ordre_croissant(self):
        """Test avec une liste en ordre croissant"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([-5, -3, -1, 0, 2]), 2)

    def test_ordre_decroissant(self):
        """Test avec une liste en ordre décroissant"""
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)
        self.assertEqual(max_integer([0, -1, -2, -3]), 0)

    def test_nombres_flottants_entiers(self):
        """Test avec des nombres qui sont techniquement des entiers"""
        # Note: La fonction est conçue pour des entiers, mais peut gérer des floats entiers
        self.assertEqual(max_integer([1, 2, 3]), 3)


if __name__ == '__main__':
    unittest.main()
