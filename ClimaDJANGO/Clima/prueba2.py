import unittest
from models import Cuenta

class TestCuentas(unittest.TestCase):

    def test_email(self):
    cta_1 = Cuenta('Orlando')
    cta_2 = Cuenta('Marcela')

    self.assertEqual(cta_1.email, 'orlando@weweather.com')
    self.assertEqual(cta_2.email, 'marcela@weweather.com')

    cta_1 = Cuenta('Orland')
    cta_2 = Cuenta('Marce')

    self.assertEqual(cta_1.email, 'orlando@weweather.com')
    self.assertEqual(cta_2.email, 'marcela@weweather.com')