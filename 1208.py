import unittest


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        current = maxCost
        answer = 0
        for right in range(len(s)):
            diff = abs(ord(s[right]) - ord(t[right]))
            current -= diff
            while current < 0 and left <= right:
                current += abs(ord(s[left]) - ord(t[left]))
                left += 1

            answer = max(right - left + 1, answer)
        return answer


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.equalSubstring("abcd", "bcdf", 3), 3)
        self.assertEqual(solution.equalSubstring("abcd", "cdef", 3), 1)
        self.assertEqual(solution.equalSubstring("abcd", "acde", 0), 1)
        self.assertEqual(solution.equalSubstring("abcd", "cdef", 1), 0)


unittest.main()
