import unittest
from typing import List
from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        seen = Counter()
        for num in nums:
            seen[num] += 1

        max_frequency = max(seen.values())
        answer = 0
        for num, frequency in seen.items():
            if frequency == max_frequency:
                answer += frequency
        return answer


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.maxFrequencyElements([1, 2, 2, 3, 1, 4]), 4)
        self.assertEqual(solution.maxFrequencyElements([1, 2, 3, 4, 5]), 5)


unittest.main()
