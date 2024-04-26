from typing import List
import unittest
        
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        right = 0
        while left < len(nums):
            if nums[left] != 0:
                nums[right] = nums[left]
                right += 1
            left += 1

        while right < len(nums):
            nums[right] = 0
            right += 1
                



        
class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        nums1 = [0,1,0,3,12]
        nums2 = [0]
        solution.moveZeroes(nums1)
        self.assertEqual(nums1, [1,3,12,0,0])
        solution.moveZeroes(nums2)
        self.assertEqual(nums2, [0])



unittest.main()
        
