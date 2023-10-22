import unittest
from main import get_telephones


class TestGetTelephoneMethod(unittest.TestCase):

    def test_search_website_repetitors(self):
         self.assertEqual(['84955405676'], get_telephones("https://repetitors.info/"))

    def test_search_website_hands(self):
         self.assertEqual(['84951370720'], get_telephones("https://hands.ru/company/about/"))

