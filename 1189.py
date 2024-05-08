import unittest


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        xs = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
        for s in text:
            if s in xs:
                xs[s] += 1

        return int(min((xs["b"], xs["a"], xs["l"] / 2, xs["o"] / 2, xs["n"])))


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.maxNumberOfBalloons("nlaebolko"), 1)
        self.assertEqual(solution.maxNumberOfBalloons("loonbalxballpoon"), 2)
        self.assertEqual(solution.maxNumberOfBalloons("leetcode"), 0)
        self.assertEqual(solution.maxNumberOfBalloons("balllllllllllloooooooooon"), 1)


unittest.main()
