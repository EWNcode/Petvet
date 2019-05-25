from django.test import TestCase

from .models import Animal


class TestAnimalCreation(TestCase):

    def test_name(self):
        self.assertAlmostEqual(Animal(5), 6)
