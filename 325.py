import unittest
from typing import List
from collections import defaultdict


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = -1
        current = 0
        right = 0
        answer = 0

        current = 0
        for right in range(len(nums)):
            current += nums[right]
            if current-k in seen:
                answer = max(answer, right - seen[current-k])
            if current not in seen:
                seen[current] = right 
        return answer


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.maxSubArrayLen([7,6,-3, 4, 2, 0, 7, -6], 3), 4)
        self.assertEqual(solution.maxSubArrayLen([1,-1,5,-2,3], 3), 4)
        self.assertEqual(solution.maxSubArrayLen([-2,-1,2,1], 1), 2)
        self.assertEqual(solution.maxSubArrayLen([1,1,0], 1), 2)


unittest.main()
