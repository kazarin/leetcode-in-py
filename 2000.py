from typing import List
from math import floor
import unittest
        
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word = list(word)
        left = 0
        for left in range(len(word)):
            if word[left] == ch:
                word[0:left+1] = word[0:left+1][::-1]
                return "".join(word)

        return "".join(word)
        
        
class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.reversePrefix("abcdefd", "d"), "dcbaefd")
        self.assertEqual(solution.reversePrefix("xyxzxe", "z"), "zxyxxe")
        self.assertEqual(solution.reversePrefix("abcd", "z"), "abcd")



unittest.main()
        
