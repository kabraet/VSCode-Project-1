import test    # The code to test
import unittest   # The test framework

class Test_TestIncrementDecrementMultiply(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(test.increment(3), 4)

    # This test is designed to fail for demonstration purposes.
    def test_decrement(self):
        self.assertEqual(test.decrement(3), 2)

    def test_square(self):
        self.assertEqual(test.square(4), 16)
    
    def test_squareroot(self):
        self.assertEqual(test.squareroot(4), 2)

if __name__ == '__main__':
    unittest.main()

