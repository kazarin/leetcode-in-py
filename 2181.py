from linked_list import ListNode, LinkedList
from typing import Optional
import unittest


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        prev = ListNode(0)
        result = prev
        while current and current.next:
            n = 0
            while current.next.val != 0:
                n = n + current.next.val
                current = current.next

            prev.next = ListNode(n)
            prev = prev.next

            current = current.next
        return result.next


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()

        self.assertEqual(
            solution.mergeNodes(LinkedList([0, 3, 1, 0, 4, 5, 2, 0]).head),
            LinkedList([4, 11]),
        )
        self.assertEqual(
            solution.mergeNodes(LinkedList([0, 1, 0, 3, 0, 2, 2, 0]).head),
            LinkedList([1, 3, 4]),
        )


unittest.main()
