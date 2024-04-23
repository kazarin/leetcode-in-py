from typing import List
from math import floor
import unittest
        
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        output = list(s)
        right = len(s) - 1
        left = 0
        while left < right:
            while not output[left].isalpha() and left < right:
                left += 1
            while not output[right].isalpha() and right > left:
                right -= 1

            output[left], output[right] = output[right], output[left]
            left += 1
            right -= 1

        return "".join(output)

class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.reverseOnlyLetters("ab-cd"), "dc-ba")
        self.assertEqual(solution.reverseOnlyLetters("a-bC-dEf-ghIj"), "j-Ih-gfE-dCba")
        self.assertEqual(solution.reverseOnlyLetters("Test1ng-Leet=code-Q!"), "Qedo1ct-eeLg=ntse-T!")



unittest.main()
        
