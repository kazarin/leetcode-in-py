import unittest


class Solution:
    def reverseWords(self, s: str) -> str:
        left = 0
        output = []
        right = 0
        for right in range(len(s)):
            if s[right] == " ":
                output.append(s[left:right][::-1])
                left = right + 1

        output.append(s[left : right + 1][::-1])
        return " ".join(output)


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(
            solution.reverseWords("Let's take LeetCode contest"),
            "s'teL ekat edoCteeL tsetnoc",
        )
        self.assertEqual(solution.reverseWords("Mr Ding"), "rM gniD")


unittest.main()
