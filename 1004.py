from typing import List
import unittest

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeroes = 0
        output = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes += 1

            while zeroes > k:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1

            output = max(output, right - left + 1)
        return output



class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2), 6)
        self.assertEqual(solution.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3), 10)


unittest.main()
        
