from typing import List
from math import floor
import unittest
        
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        left = 0
        right = 0
        while left < len(nums1) and right < len(nums2):
            if nums1[left] == nums2[right]:
                return nums1[left]
            if nums1[left] > nums2[right]:
                right += 1
            else:
                left += 1

        return -1
        
class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.getCommon([1,2,3], [2,4]), 2)
        self.assertEqual(solution.getCommon([1,2,3,6], [2,3,4,5]), 2)
        self.assertEqual(solution.getCommon([7,8,9], [2,3,4]), -1)



unittest.main()
        
