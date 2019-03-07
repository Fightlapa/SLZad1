import unittest
from JezykiSkryptowe1 import my_oct, SIZE, EXTREME_VALUE

class Test_myocctest(unittest.TestCase):
    def test_my_oct(self):
        for i in range (-SIZE, SIZE):
            self.assertEqual(my_oct(i), oct(i))
        self.assertEqual(my_oct(EXTREME_VALUE), oct(EXTREME_VALUE))

if __name__ == '__main__':
    unittest.main()
