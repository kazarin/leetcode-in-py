from typing import List
from collections import defaultdict
import unittest


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        answer = -1
        for num in nums:
            n = sum(map(int, str(num)))
            if n in seen:
                answer = max(answer, num + seen[n])
            seen[n] = max(seen[n], num)

        return answer


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.maximumSum([18, 43, 36, 13, 7]), 54)
        self.assertEqual(solution.maximumSum([10, 12, 19, 14]), -1)


unittest.main()
