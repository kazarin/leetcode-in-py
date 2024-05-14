from typing import List
import unittest
from collections import defaultdict


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        right = 0
        seen = defaultdict(int)
        answer = float("inf")
        for right in range(len(cards)):
            if cards[right] in seen:
                answer = min(answer, right - seen[cards[right]] + 1)
            seen[cards[right]] = right
        if answer == float("inf"):
            return -1
        return answer


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.minimumCardPickup([3, 4, 2, 3, 4, 7]), 4)
        self.assertEqual(solution.minimumCardPickup([1, 0, 5, 3]), -1)


unittest.main()
