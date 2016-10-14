import unittest

import dice


class DieTests(unittest.TestCase):
    def setUp(self):
        self.d6 = dice.Die(6)
        self.d8 = dice.Die(8)
        
    def test_creation(self):
        self.assertEqual(self.d6.sides, 6)
        self.assertIn(self.d6.value, range(1,7))
        
    def test_add(self):
        self.assertIsInstance(self.d6+self.d8, int)
        
    def test_bad_sides(self):
        with self.assertRaises(ValueError):
            dice.Die(1)
        
        
class RollTests(unittest.TestCase):
    def setUp(self):
        self.hand1 = dice.Roll('1d2')
        self.hand3 = dice.Roll('3d6')
        
    def test_lower(self):
        self.assertGreaterEqual(int(self.hand3), 3)
        
    def test_upper(self):
        self.assertLessEqual(int(self.hand3), 18)
        
    def test_membership(self):
        test_die = dice.Die(2)
        test_die.value = self.hand1.results[0].value
        self.assertIn(test_die, self.hand1.results)
        
    def test_bad_description(self):
        with self.assertRaises(ValueError):
            dice.Roll('2b6')
            
    def test_adding(self):
        self.assertEqual(self.hand1+self.hand3, 
                         sum(self.hand1.results)+sum(self.hand3.results))
            
if __name__ == '__main__':
    unittest.main()