import unittest
from keb import Solution

class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minEatingSpeed1(self):
        piles = [3, 6, 7, 11]
        h = 8
        expected = 4
        self.assertTrue(self.solution.minEatingSpeed(piles, h) == expected)

    def test_minEatingSpeed2(self):
        piles = [30, 11, 23, 4, 20]
        h = 5
        expected = 30
        self.assertTrue(self.solution.minEatingSpeed(piles, h) == expected)

    def test_minEatingSpeed3(self):
        piles = [30, 11, 23, 4, 20]
        h = 6
        expected = 23
        self.assertTrue(self.solution.minEatingSpeed(piles, h) == expected)

    def test_minEatingSpeed4(self):
        piles = [5, 10, 15, 20]
        h = 100
        expected = 0
        self.assertFalse(self.solution.minEatingSpeed(piles, h) == expected)

    def test_minEatingSpeed5(self):
        piles = [5, 10, 15, 20]
        h = -5
        expected = 5
        self.assertFalse(self.solution.minEatingSpeed(piles, h) == expected)

if __name__ == '__main__':
    unittest.main()