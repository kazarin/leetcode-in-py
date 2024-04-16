from typing import List
import unittest
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        left = 0
        right = len(nums)-1

        for i in range(len(nums)-1, -1, -1):
            a = nums[left] * nums[left]
            b = nums[right] * nums[right]
            if a > b:
                output[i] = a
                left += 1
            else:
                output[i] = b
                right -= 1

        return output



class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.sortedSquares([-4,-1,0,3,10]), [0,1,9,16,100])
        self.assertEqual(solution.sortedSquares([-7,-3,2,3,11]), [4,9,9,49,121])


unittest.main()
        
