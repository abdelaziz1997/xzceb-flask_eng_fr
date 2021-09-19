import unittest
import sys
sys.path.append("..")

from translator import english_to_french, french_to_english
class TestEnglishTranslator(unittest.TestCase): 
    def testEnglish2FrenchTranslator(self):
        self.assertEqual(english_to_french(None), None)
        self.assertEqual(english_to_french('Hello'), 'Bonjour') 
        self.assertEqual(english_to_french('Kitchen'), 'Cuisine') 
        self.assertEqual(english_to_french('House'), 'Maison') 

class TestFrenchTranslator(unittest.TestCase): 
    def testFrench2EnglishTranslator(self): 
        self.assertEqual(french_to_english(None), None)      
        self.assertEqual(french_to_english('Bonjour'), 'Hello') 
        self.assertEqual(french_to_english('Cuisine'), 'Kitchen') 
        self.assertEqual(french_to_english('Maison'), 'House')  

unittest.main()
