import unittest
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        seen = {}
        for path in paths:
            seen[path[0]] = path[1]

        n = seen[paths[0][0]]
        while n in seen:
            n = seen[n]

        return n


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(
            solution.destCity(
                [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
            ),
            "Sao Paulo",
        )
        self.assertEqual(solution.destCity([["B", "C"], ["D", "B"], ["C", "A"]]), "A")
        self.assertEqual(solution.destCity([["A", "Z"]]), "Z")


unittest.main()
