from typing import List
import unittest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, n in enumerate(nums):
            x = h.get(target - n)
            if x != None:
                return [i, x]
            h[n] = i


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertCountEqual(solution.twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertCountEqual(solution.twoSum([3, 2, 4], 6), [1, 2])
        self.assertCountEqual(solution.twoSum([3, 3], 6), [0, 1])


unittest.main()
