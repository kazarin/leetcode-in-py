import unittest
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        seen = Counter(s)

        answer = []
        for letter, freq in sorted(
            seen.items(), key=lambda item: item[1], reverse=True
        ):
            answer.append(letter * freq)

        return "".join(answer)


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.frequencySort("tree"), "eetr")
        self.assertEqual(solution.frequencySort("cccaaa"), "cccaaa")
        self.assertEqual(solution.frequencySort("Aabb"), "bbAa")


unittest.main()
