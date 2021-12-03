import unittest

from translator import english_to_french
from translator import french_to_english

class Test_english_to_french(unittest.TestCase): 
   
    def test_english_to_french1(self): 
        self.assertEqual(english_to_french('Rice'), 'Riz')   
    def test_english_to_french2(self):
        self.assertEqual(english_to_french('Flag'), 'Drapeau') 
    def test_hello_to_bonjour(self):
        self.assertNotEqual(english_to_french('hello'), 'Non')
    def test_null_to_french(self):
        self.assertNotEqual(english_to_french(0), 0)

    
class Test_french_to_english(unittest.TestCase): 

    def test_french_to_english1(self): 
        self.assertEqual(french_to_english('travail'), 'Job')    
    def test_french_to_english2(self): 
        self.assertEqual(french_to_english('Sommeil'), 'Sleep')
    def test_bonjour_to_hello(self): 
        self.assertNotEqual(french_to_english('bonjour'), 'Person')
    def test_null_to_english1(self): 
        self.assertNotEqual(french_to_english(0), 0) 
unittest.main()
