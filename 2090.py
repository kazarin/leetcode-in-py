from typing import List
from math import floor
import unittest
        
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        sums = [nums[0]]

        for i in range(1, len(nums)):
            sums.append(sums[-1] + nums[i])

        output = []
        for i in range(len(nums)):
            if i < k or i >= len(nums)-k:
                output.append(-1)
            else:
                output.append(floor((sums[i+k]-sums[i-k]+nums[i-k]) / (k * 2 + 1)))

        return output

class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.getAverages([7,4,3,9,1,8,5,2,6], 3), [-1,-1,-1,5,4,4,-1,-1,-1])
        self.assertEqual(solution.getAverages([100000], 0), [100000])
        self.assertEqual(solution.getAverages([8], 100000), [-1])



unittest.main()
        
