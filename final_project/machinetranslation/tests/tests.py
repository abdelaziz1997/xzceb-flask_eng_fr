import unittest

import machinetranslation
 
class TestEnglishTranslator(unittest.TestCase): 
    def testEnglish2FrenchTranslator(self):
        englishTextExample1 = input("Enter the english text to translate to french: ")
        nullInput = None
        self.assertIsNotNone(englishTextExample1, english_to_french(englishTextExample1))
        self.assertIsNone(nullInput, english_to_french(nullInput))
        self.assertEqual(english_to_french('Hello'), 'Bonjour') 
        self.assertEqual(english_to_french('Kitchen'), 'Cuisine') 
        self.assertEqual(english_to_french('House'), 'Maison') 

class TestFrenchTranslator(unittest.TestCase): 
    def testFrench2EnglishTranslator(self): 
        frenchTextExample1 = input("Enter the french text to translate to english: ")
        nullInput = None
        self.assertIsNotNone(frenchTextExample1, french_to_english(frenchTextExample1))
        self.assertIsNone(nullInput, french_to_english(nullInput))      
        self.assertEqual(french_to_english('Bonjour'), 'Hello') 
        self.assertEqual(french_to_english('Cuisine'), 'Kitchen') 
        self.assertEqual(french_to_english('Maison'), 'House')  

unittest.main()