from typing import List
import unittest
        
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sums = [0, gain[0]]
        answer = 0
        for left in range(1, len(gain)):
            sums.append(sums[-1] + gain[left])

        return max(sums)
        
class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.largestAltitude([-5,1,5,0,-7]), 1)
        self.assertEqual(solution.largestAltitude([-4,-3,-2,-1,4,3,2]), 0)

unittest.main()
        
