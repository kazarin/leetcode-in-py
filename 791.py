import unittest
from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        letters = Counter(s)

        output = [token for token in order for _ in range(letters[token])]
        remaining = [token for token in s if token not in order]

        return "".join(output + remaining)


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.customSortString("cba", "abcd"), "cbad")
        self.assertEqual(solution.customSortString("bcafg", "abcd"), "bcad")


unittest.main()
