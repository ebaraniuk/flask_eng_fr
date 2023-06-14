import unittest
from machinetranslation.translator import french_to_english, english_to_french


class TestTranslator(unittest.TestCase):

    def test_translate(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')


if __name__ == '__main__':
    TestTranslator().test_translate()
