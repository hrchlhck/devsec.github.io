from unittest import TestCase

from main import index, ola, APP

class TestePaginas(TestCase):
    def test_index(self):   
        self.assertEqual(index(), "<h1>Docker</h1>")

    def test_ola(self):
        self.assertEqual(ola(), "<h1>Olá, mundo!</h1>")

    def test_debug(self):
        self.assertFalse(APP.debug)