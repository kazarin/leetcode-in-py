import unittest

from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        xs = defaultdict(int)
        xs[0] = 1
        current = 0
        answer = 0
        for num in nums:
            current += num
            answer += xs[current - k]
            xs[current] += 1

        return answer


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.subarraySum([1, 1, 1], 2), 2)
        self.assertEqual(solution.subarraySum([1, 2, 3], 3), 2)


unittest.main()
