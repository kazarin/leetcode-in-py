from typing import List
import unittest


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = [nums[0]]
        for i in range(1, len(nums)):
            output.append(nums[i] + output[i - 1])
        return output


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.runningSum([1, 2, 3, 4]), [1, 3, 6, 10])
        self.assertEqual(solution.runningSum([1, 1, 1, 1, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(solution.runningSum([3, 1, 2, 10, 1]), [3, 4, 6, 16, 17])


unittest.main()
