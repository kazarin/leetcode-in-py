import unittest
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for s in strs:
            key = str(sorted(s))
            seen[key].append(s)

        return seen.values()


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertCountEqual(
            solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        )
        self.assertCountEqual(solution.groupAnagrams([""]), [[""]])


unittest.main()
