import unittest
import calc
from models import TipoUser
class TestCalcu(unittest.TestCase):


    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

     def test_subtract(self):
            self.assertEqual(calc.subtract(10, 5), 5)
            self.assertEqual(calc.subtract(-1, 1), -2)
            self.assertEqual(calc.subtract(-1, -1), 0)



class testUser(unittest.TestCase):

    def test_user(self):
    user_1 = TipoUser('Orlando', 1)
    user_2 = TipoUser('Marcela', 2)

    self.assertEqual(user_1.user, ('Orlando', 1)
    self.assertEqual(user_1.user, ('Marcela', 2)

        user_1 = Cuenta('Orland' ,1)
        user_2 = Cuenta('Marce', 2)

     self.assertEqual(user_1.user, ('Orlando', 1)
     self.assertEqual(user_1.user, ('Marcela', 2)
