import unittest
import os

from beprof import profile


class TestFunMethod(unittest.TestCase):
    def test_check(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
