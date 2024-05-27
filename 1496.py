import unittest


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = y = 0
        seen = set()
        seen.add((0, 0))
        for d in path:
            match d:
                case "N":
                    y += 1
                case "S":
                    y -= 1
                case "W":
                    x -= 1
                case "E":
                    x += 1
            if (x, y) in seen:
                return True
            seen.add((x, y))

        return False


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(solution.isPathCrossing("NES"), False)
        self.assertEqual(solution.isPathCrossing("NESWW"), True)


unittest.main()
