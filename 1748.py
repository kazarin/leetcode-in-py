import unittest
from typing import List
from collections import Counter


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        seen = Counter()
        answer = 0
        for num in nums:
            seen[num] += 1

        for num, occurences in seen.items():
            if occurences == 1:
                answer += num
        return answer


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.sumOfUnique([1, 2, 3, 2]), 4)
        self.assertEqual(solution.sumOfUnique([1, 1, 1, 1, 1]), 0)
        self.assertEqual(solution.sumOfUnique([1, 2, 3, 4, 5]), 15)


unittest.main()
