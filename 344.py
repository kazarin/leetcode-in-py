from typing import List
import unittest


class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        s1 = ["h", "e", "l", "l", "o"]
        solution.reverseString(s1)
        self.assertEqual(s1, ["o", "l", "l", "e", "h"])

        s2 = ["H", "a", "n", "n", "a", "h"]
        solution.reverseString(s2)
        self.assertEqual(s2, ["h", "a", "n", "n", "a", "H"])


unittest.main()
