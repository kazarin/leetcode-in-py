from typing import List
from collections import defaultdict
import unittest


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        xs = defaultdict(int)
        for num in nums:
            xs[num] += 1
        once = [k for k, v in xs.items() if v == 1]
        if len(once) == 0:
            return -1
        else:
            return max(once)


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.largestUniqueNumber([5, 7, 3, 9, 4, 9, 8, 3, 1]), 8)
        self.assertEqual(solution.largestUniqueNumber([9, 9, 8, 8]), -1)


unittest.main()
