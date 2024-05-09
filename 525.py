import unittest
from typing import List
from collections import defaultdict


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        xs = defaultdict(int)
        xs[0] = -1
        current = 0
        answer = 0

        for right in range(len(nums)):
            if nums[right] == 1:
                current += 1
            else:
                current -= 1
            if current in xs:
                answer = max(answer, right - xs[current])
            else:
                xs[current] = right

        return answer


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.findMaxLength([0, 1, 0, 1, 0, 0, 1, 1]), 8)
        self.assertEqual(solution.findMaxLength([0, 1]), 2)
        self.assertEqual(solution.findMaxLength([0, 1, 0]), 2)


unittest.main()
