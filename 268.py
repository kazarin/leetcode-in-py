import unittest
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(0, len(nums) + 1)) - sum(nums)


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.missingNumber([3, 0, 1]), 2)
        self.assertEqual(solution.missingNumber([0, 1]), 2)
        self.assertEqual(solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)


unittest.main()
