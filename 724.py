from typing import List
import unittest


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sums = [nums[0]]
        for left in range(1, len(nums)):
            sums.append(sums[-1] + nums[left])

        for left in range(len(nums)):
            if sums[left] == sums[-1] - sums[left] + nums[left]:
                return left

        return -1


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.pivotIndex([1, 7, 3, 6, 5, 6]), 3)
        self.assertEqual(solution.pivotIndex([1, 2, 3]), -1)
        self.assertEqual(solution.pivotIndex([2, 1, -1]), 0)


unittest.main()
