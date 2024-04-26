from typing import List
import unittest


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefixes = [nums[0]]
        for i in range(1, len(nums)):
            prefixes.append(prefixes[-1] + nums[i])
        output = 0
        for i in range(len(nums) - 1):
            if prefixes[i] >= prefixes[-1] - prefixes[i + 1] + nums[i + 1]:
                output += 1

        return output


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.waysToSplitArray([10, 4, -8, 7]), 2)
        self.assertEqual(solution.waysToSplitArray([2, 3, 1, 0]), 2)
        self.assertEqual(solution.waysToSplitArray([0, 0]), 1)


unittest.main()
