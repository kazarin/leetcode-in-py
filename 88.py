import unittest
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = j = x = 0
        nums1_original = nums1[:m]

        while i < m and j < n:
            if nums1_original[i] < nums2[j]:
                nums1[x] = nums1_original[i]
                i += 1
            else:
                nums1[x] = nums2[j]
                j += 1
            x += 1

        while i < m:
            nums1[x] = nums1_original[i]
            i += 1
            x += 1
        while j < n:
            nums1[x] = nums2[j]
            j += 1
            x += 1


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        nums_a = [1, 2, 3, 0, 0, 0]
        solution.merge(nums_a, 3, [2, 5, 6], 3)
        self.assertEqual(nums_a, [1, 2, 2, 3, 5, 6])

        nums_b = [1]
        solution.merge(nums_b, 1, [], 0)
        self.assertEqual(nums_b, [1])


unittest.main()
