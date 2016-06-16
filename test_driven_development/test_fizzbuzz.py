import unittest
import Fizzbuzz
#from test_driven_development import Fizzbuzz
class fizzBuzz(unittest.TestCase):
     """Testing fizzbuzz"""
     def test_returns_fizz_divisible_by_three(self):
         """Teat return fizz when number id divisible by three"""
         self.assertEqual(Fizzbuzz.fizz_buzz, 'fizz')
     def test_returns_buzz_divisible_by_three(self):
         """This method returns buzz when number id divisible by five"""
         self.assertEqual(Fizzbuzz.fizz_buzz(5),'buzz')
     def test_returns_fizzbuzz_divisible_by_both(self):
                  """This method returns buzz when number id divisible by five"""
                  self.assertEqual(Fizzbuzz.fizz_buzz(15),'fizzbuzz')