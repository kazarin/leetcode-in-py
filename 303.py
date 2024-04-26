from typing import List
import unittest


class NumArray:
    def __init__(self, nums: List[int]):
        self.sums = [nums[0]]
        self.nums = nums
        for i in range(1, len(nums)):
            self.sums.append(self.sums[-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right] - self.sums[left] + self.nums[left]


class TestSolution(unittest.TestCase):
    def runTest(self):
        cmd = ["NumArray", "sumRange", "sumRange", "sumRange"]
        args = [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]

        instance = NumArray(*args[0])
        expected = [None]
        for cmd, args in zip(cmd[1:], args[1:]):
            method = getattr(instance, cmd)
            expected.append(method(*args))

        self.assertEqual(expected, [None, 1, -1, -3])


unittest.main()
