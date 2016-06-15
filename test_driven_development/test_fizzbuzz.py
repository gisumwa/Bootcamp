import unittest
import Fizzbuzz
#from test_driven_development import Fizzbuzz
class fizzBuzz(unittest.TestCase):
     """Testing fizzbuzz"""
     def test_returns_fizz_divisible_by_three(self):
         """Teat return fizz when number id divisible by three"""
         self.assertEqual(Fizzbuzz.fizz_buzz(3), 'fizz')
         self.assertEqual(Fizzbuzz.fizz_buzz(5),'buzz')
         self.assertEqual(Fizzbuzz.fizz_buzz(15),'fizzbuzz')
