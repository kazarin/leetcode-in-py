import unittest


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        visited = set()
        for i in range(len(s)):
            if s[i] in visited:
                return s[i]

            visited.add(s[i])
        return s


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.repeatedCharacter("abccbaacz"), "c")
        self.assertEqual(solution.repeatedCharacter("abcdd"), "d")



unittest.main()
