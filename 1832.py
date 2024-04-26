import unittest


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = set(sentence)
        return len(letters) == 26


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"), True)
        self.assertEqual(solution.checkIfPangram("leetcode"), False)



unittest.main()
