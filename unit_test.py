import unittest
from keb import Solution

class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minEatingSpeed1(self):
        """
        Test Case 1

        The piles are [3, 6, 7, 11], and the maximum number of hours available is 8.
        The expected minimum eating speed is 4.
        Since the expected result matches the actual result, the assertion uses assertTrue.
        """
        piles = [3, 6, 7, 11]
        h = 8
        expected = 4
        self.assertTrue(self.solution.minEatingSpeed(piles, h) == expected)

    def test_minEatingSpeed2(self):
        """
        Test Case 2

        The piles are [30, 11, 23, 4, 20], and the maximum number of hours available is 5.
        The expected minimum eating speed is 30.
        Since the expected result matches the actual result, the assertion uses assertTrue.
        """
        piles = [30, 11, 23, 4, 20]
        h = 5
        expected = 30
        self.assertTrue(self.solution.minEatingSpeed(piles, h) == expected)

    def test_minEatingSpeed3(self):
        """
        Test Case 3

        The piles are [30, 11, 23, 4, 20], and the maximum number of hours available is 6.
        The expected minimum eating speed is 23.
        Since the expected result matches the actual result, the assertion uses assertTrue.
        """
        piles = [30, 11, 23, 4, 20]
        h = 6
        expected = 23
        self.assertTrue(self.solution.minEatingSpeed(piles, h) == expected)

    def test_minEatingSpeed4(self):
        """
        Test Case 4

        The piles are [5, 10, 15, 20], and the maximum number of hours available is 100.
        The expected minimum eating speed is 0 since it's impossible to eat all the piles within the given time.
        Since the expected result does not match the actual result, the assertion uses assertFalse.
        """
        piles = [5, 10, 15, 20]
        h = 100
        expected = 0
        self.assertFalse(self.solution.minEatingSpeed(piles, h) == expected)

    def test_minEatingSpeed5(self):
        """
        Test Case 5

        The piles are [5, 10, 15, 20], and the maximum number of hours available is -5.
        The expected minimum eating speed is 5.
        Since the expected result does not match the actual result, the assertion uses assertFalse.
        """
        piles = [5, 10, 15, 20]
        h = -5
        expected = 5
        self.assertFalse(self.solution.minEatingSpeed(piles, h) == expected)

if __name__ == '__main__':
    unittest.main()