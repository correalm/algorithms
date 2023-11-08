import unittest

from expression import expression

class TestExpressionFunction(unittest.TestCase):
    def test_expression(self):
        self.assertEqual(expression(1,2,3), 9)
        self.assertEqual(expression(2,10,3), 60)
        self.assertEqual(expression(10,10,10), 1000)
        self.assertEqual(expression(3,3,3), 27)

if __name__ == '__main__':
    unittest.main()