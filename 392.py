import unittest
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.isSubsequence("abc", "ahbgdc"), True)
        self.assertEqual(solution.isSubsequence("axc", "ahbgdc"), False)


unittest.main()
        
