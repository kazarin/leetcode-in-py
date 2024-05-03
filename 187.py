import unittest
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        left = 0
        right = 10
        xs = set()
        output = set()

        while right <= len(s):
            seq = s[left:right]
            if seq in xs:
                output.add(seq)

            xs.add(seq)
            left += 1
            right += 1

        return output


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertCountEqual(
            solution.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"),
            ["AAAAACCCCC", "CCCCCAAAAA"],
        )
        self.assertCountEqual(
            solution.findRepeatedDnaSequences("AAAAAAAAAAAAA"), ["AAAAAAAAAA"]
        )
        self.assertCountEqual(
            solution.findRepeatedDnaSequences("AAAAAAAAAAA"), ["AAAAAAAAAA"]
        )


unittest.main()
