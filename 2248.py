import unittest

from typing import List
from collections import defaultdict


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        xs = defaultdict(int)
        for row in nums:
            for el in row:
                xs[el] += 1

        output = []
        for k, v in xs.items():
            if v == len(nums):
                output.append(k)
        return sorted(output)


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(
            solution.intersection([[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]), [3, 4]
        )
        self.assertEqual(solution.intersection([[1, 2, 3], [4, 5, 6]]), [])


unittest.main()
