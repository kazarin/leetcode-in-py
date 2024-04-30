import unittest
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        xs = defaultdict(int)
        left = 0
        answer = 0
        for right in range(len(s)):
            xs[s[right]] += 1
            while len(xs) > k:
                xs[s[left]] -= 1
                if xs[s[left]] == 0:
                    del xs[s[left]]
                left += 1
            answer = max(answer, right - left + 1)

        return answer


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.lengthOfLongestSubstringKDistinct("eceba", 2), 3)
        self.assertEqual(solution.lengthOfLongestSubstringKDistinct("aa", 1), 2)


unittest.main()
