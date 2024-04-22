from typing import List
import unittest
        
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefixes = [nums[0]]
        for i in range(1, len(nums)):
            prefixes.append(nums[i] + prefixes[i-1])
        m = 1 - min(prefixes)
        if m <= 0:
            return 1
        else:
            return m



class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.minStartValue([-3,2,-3,4,2]), 5)
        self.assertEqual(solution.minStartValue([1,2]), 1)
        self.assertEqual(solution.minStartValue([1,-2,-3]), 5)
        self.assertEqual(solution.minStartValue([2,3,5,-5,-1]), 1)



unittest.main()
        
