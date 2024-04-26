import unittest


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        left = 0
        current = 0
        answer = 0
        for right in range(len(s)):
            if s[right] in vowels:
                current += 1

            while right - left + 1 > k:
                if s[left] in vowels:
                    current -= 1
                left += 1

            answer = max(answer, current)

        return answer


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.maxVowels("abciiidef", 3), 3)
        self.assertEqual(solution.maxVowels("aeiou", 2), 2)
        self.assertEqual(solution.maxVowels("leetcode", 3), 2)


unittest.main()
