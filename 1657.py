import unittest
from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        occ1 = Counter(word1)
        occ2 = Counter(word2)

        if set(occ1.keys()) != set(occ2.keys()):
            return False
        if sorted(occ1.values()) != sorted(occ2.values()):
            return False
        return True


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.closeStrings("abc", "bca"), True)
        self.assertEqual(solution.closeStrings("a", "aa"), False)
        self.assertEqual(solution.closeStrings("cabbba", "abbccc"), True)
        self.assertEqual(solution.closeStrings("abbzzca", "babzzcz"), False)


unittest.main()
