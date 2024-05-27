import unittest
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.containsDuplicate([1, 2, 3, 1]), True)
        self.assertEqual(solution.containsDuplicate([1, 2, 3, 4]), False)
        self.assertEqual(
            solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True
        )


unittest.main()
