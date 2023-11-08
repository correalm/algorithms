import unittest

from even_odds import even_odds

class TestEvenOddsFunction(unittest.TestCase):
    def test_even_odds(self):
        self.assertEqual(even_odds(10, 3), 5)
        self.assertEqual(even_odds(7, 7), 6)

if __name__ == '__main__':
    unittest.main()