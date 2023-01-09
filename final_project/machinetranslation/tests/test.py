import unittest
from translator import frenchToEnglish, englishToFrench

class testfrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual('Bonjour', 'Hello')

class testenglishToFrench(unittest.TestCase):
    def test2(self):
        self.assertEqual('Hello', 'Bonjour')

unittest.main()