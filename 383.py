import unittest
from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = defaultdict(int)

        for s in magazine:
            letters[s] += 1

        for s in ransomNote:
            if letters[s] == 0:
                return False
            else:
                letters[s] -= 1

        return True


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.canConstruct("a", "b"), False)
        self.assertEqual(solution.canConstruct("aa", "ab"), False)
        self.assertEqual(solution.canConstruct("aa", "aab"), True)


unittest.main()
