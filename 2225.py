from typing import List
from collections import defaultdict
import unittest


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losers = defaultdict(int)
        for match in matches:
            w = match[0]
            loser = match[1]
            winners.add(w)
            losers[loser] += 1

        return [
            sorted([n for n in winners if n not in losers]),
            sorted([n for n, loses in losers.items() if loses == 1]),
        ]


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(
            solution.findWinners(
                [
                    [1, 3],
                    [2, 3],
                    [3, 6],
                    [5, 6],
                    [5, 7],
                    [4, 5],
                    [4, 8],
                    [4, 9],
                    [10, 4],
                    [10, 9],
                ]
            ),
            [[1, 2, 10], [4, 5, 7, 8]],
        )


unittest.main()
