import unittest
from translator import englishToFrench, frenchToEnglish
class TestenglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour") #Already Checked
        self.assertEqual(englishToFrench("Love"), "Amour")
        self.assertEqual(englishToFrench("Sky"), "Ciel")
        self.assertEqual(englishToFrench("Flower"), "Fleur")

class TestfrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello") #Already Checked
        self.assertEqual((frenchToEnglish("Amour"), "Love")
        self.assertEqual((frenchToEnglish("Ciel"), "Sky")
        self.assertEqual((frenchToEnglish("Fleur"), "Flower")
        
unittest.main()