import unittest

from collections import defaultdict


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        xs = defaultdict(int)
        for sym in s:
            xs[sym] += 1
        occurences = set(xs.values())
        return len(occurences) == 1


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.areOccurrencesEqual("abacbc"), True)
        self.assertEqual(solution.areOccurrencesEqual("aaabb"), False)


unittest.main()
