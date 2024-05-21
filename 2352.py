import unittest
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cols = list(map(list, zip(*grid)))
        output = 0
        for row in grid:
            for col in cols:
                if row == col:
                    output += 1

        return output


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]), 1)
        self.assertEqual(
            solution.equalPairs(
                [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
            ),
            3,
        )


unittest.main()
