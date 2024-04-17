from typing import List
import unittest
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        output = left = 0
        product = 1

        for right in range(len(nums)):
            product *= nums[right]
            while product >= k:
                product /= nums[left]
                left += 1
            output += right-left + 1

        return output
        

class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.numSubarrayProductLessThanK([10,5,2,6], 100), 8)
        self.assertEqual(solution.numSubarrayProductLessThanK([1,2,3], 0), 0)



unittest.main()
        
