from typing import List
import unittest


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        s = 0
        right = 0
        while right < k:
            s += nums[right]
            right += 1

        avg = s / k

        while right < len(nums):
            s += nums[right] - nums[left]
            right += 1
            left += 1
            avg = max(avg, s / k)

        return avg


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4), 12.75)
        self.assertEqual(solution.findMaxAverage([5], 1), 5.0)


unittest.main()
