from typing import Optional
from linked_list import ListNode, LinkedList
import unittest


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = head
        while h:
            while h.next and h.next.val == h.val:
                h.next = h.next.next
            h = h.next
        return head


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()

        self.assertEqual(
            solution.deleteDuplicates(LinkedList([1, 1, 1, 2, 2, 2]).head),
            LinkedList([1, 2]),
        )
        self.assertEqual(
            solution.deleteDuplicates(LinkedList([1, 1, 2, 3, 3]).head),
            LinkedList([1, 2, 3]),
        )


unittest.main()
