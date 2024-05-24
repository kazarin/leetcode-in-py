import unittest
from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = Counter()
        left = 0
        answer = 0

        for right in range(len(s)):
            seen[s[right]] += 1
            while seen[s[right]] > 1:
                seen[s[left]] -= 1
                left += 1

            answer = max(answer, right - left + 1)
        return answer


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(solution.lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(solution.lengthOfLongestSubstring("pwwkew"), 3)


unittest.main()
