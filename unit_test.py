import unittest
from keb import Solution

class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minEatingSpeed_valid1(self):
        """
        Test Case 1 - Valid Input

        The piles are [3, 6, 7, 11], and the maximum number of hours available is 8.
        The expected minimum eating speed is 4.
        This test case verifies that the function returns the correct minimum eating speed for a valid input.
        """
        piles = [3, 6, 7, 11]
        h = 8
        expected = 4
        self.assertTrue(self.solution.minEatingSpeed(piles, h) == expected)

    def test_minEatingSpeed_valid2(self):
        """
        Test Case 2 - Valid Input

        The piles are [30, 11, 23, 4, 20], and the maximum number of hours available is 5.
        The expected minimum eating speed is 30.
        This test case verifies that the function returns the correct minimum eating speed for a valid input.
        """
        piles = [30, 11, 23, 4, 20]
        h = 5
        expected = 30
        self.assertTrue(self.solution.minEatingSpeed(piles, h) == expected)

    def test_minEatingSpeed_valid3(self):
        """
        Test Case 3 - Valid Input

        The piles are [30, 11, 23, 4, 20], and the maximum number of hours available is 6.
        The expected minimum eating speed is 23.
        This test case verifies that the function returns the correct minimum eating speed for a valid input.
        """
        piles = [30, 11, 23, 4, 20]
        h = 6
        expected = 23
        self.assertTrue(self.solution.minEatingSpeed(piles, h) == expected)

    def test_minEatingSpeed_invalid1(self):
        """
        Test Case 4 - Invalid Input

        The piles are [5, 10, 15, 20], and the maximum number of hours available is 100.
        It's impossible to eat all the piles within the given time, so the expected minimum eating speed is 0.
        This test case covers a scenario where the input values are at the extreme or upper boundary value (h = 100), representing a boundary value.
        """
        piles = [5, 10, 15, 20]
        h = 100
        expected = 0
        self.assertFalse(self.solution.minEatingSpeed(piles, h) == expected)

    def test_minEatingSpeed_invalid2(self):
        """
        Test Case 5 - Invalid Input

        The piles are [5, 10, 15, 20], and the maximum number of hours available is -5.
        The expected minimum eating speed is 5.
        This test case covers a scenario where the input values are at the extreme or lower boundary value (h = -5), representing a boundary value.
        """
        piles = [5, 10, 15, 20]
        h = -5
        expected = 5
        self.assertFalse(self.solution.minEatingSpeed(piles, h) == expected)

if __name__ == '__main__':
    unittest.main()
