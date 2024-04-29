import unittest
from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        elems = set(arr)

        answer = 0
        for k in arr:
            if k + 1 in elems:
                answer += 1
        return answer


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.countElements([1, 2, 3]), 2)
        self.assertEqual(solution.countElements([1, 1, 3, 3, 5, 5, 7, 7]), 0)
        self.assertEqual(solution.countElements([1, 2, 3, 1]), 3)


unittest.main()
