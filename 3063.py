from linked_list import ListNode, LinkedList
from collections import Counter
from typing import Optional
import unittest


class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = Counter()
        current = head
        prev = None
        while current:
            if current.val in seen:
                node = seen[current.val]
                node.val += 1
            else:
                seen[current.val] = ListNode(1, prev)
                prev = seen[current.val]

            current = current.next

        return prev


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()

        self.assertEqual(
            solution.frequenciesOfElements(LinkedList([1, 1, 2, 1, 2, 3]).head),
            LinkedList([3, 2, 1]),
        )


unittest.main()
