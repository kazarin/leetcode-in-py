import unittest


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_t = {}
        t_p = {}
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        for p, t in zip(pattern, words):
            if (p not in p_t) and (t not in t_p):
                p_t[p] = t
                t_p[t] = p
            elif p_t.get(p) != t or t_p.get(t) != p:
                return False

        return True


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.wordPattern("abba", "dog cat cat dog"), True)
        self.assertEqual(solution.wordPattern("abba", "dog cat cat fish"), False)
        self.assertEqual(solution.wordPattern("aaaa", "dog cat cat dog"), False)
        self.assertEqual(solution.wordPattern("aaa", "aa aa aa aa"), False)


unittest.main()
