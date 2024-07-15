from typing import List
from collections import defaultdict
import unittest
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t = {}
        t_s = {}
        for a, b in zip(s, t):
            if (a not in s_t) and (b not in t_s):
                s_t[a] = b
                t_s[b] = a
            elif s_t.get(a) != b or t_s.get(b) != a:
                return False

        return True
        




class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.isIsomorphic("egg", "add"), True)
        self.assertEqual(solution.isIsomorphic("foo", "bar"), False)
        self.assertEqual(solution.isIsomorphic("paper", "title"), True)
        self.assertEqual(solution.isIsomorphic("badc", "baba"), False)


unittest.main()
