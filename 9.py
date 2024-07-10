import unittest


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x % 10 == 0:
            return False

        reversed_number = 0

        while x != 0:
            last_digit = x % 10
            reversed_number = reversed_number * 10 + last_digit
            x = x // 10

        return reversed_number == x or x == reversed_number // 10


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.isPalindrome(121), True)
        self.assertEqual(solution.isPalindrome(-121), False)
        self.assertEqual(solution.isPalindrome(10), False)


unittest.main()
