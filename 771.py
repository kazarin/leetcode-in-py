import unittest
from collections import defaultdict


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        xs = defaultdict(int)
        for stone in stones:
            xs[stone] += 1

        output = 0
        for jewel in jewels:
            output += xs[jewel]
        return output


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.numJewelsInStones("aA", "aAAbbbb"), 3)
        self.assertEqual(solution.numJewelsInStones("z", "ZZ"), 0)


unittest.main()
