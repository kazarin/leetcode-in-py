from linked_list import ListNode, LinkedList
from typing import Optional
import unittest


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None

        slow = fast = head
        prev = ListNode(0)
        prev.next = head
        while fast and fast.next:
            prev = prev.next
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next
        return head


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()

        self.assertEqual(
            solution.deleteMiddle(LinkedList([1, 3, 4, 7, 1, 2, 6]).head),
            LinkedList([1, 3, 4, 1, 2, 6]),
        )


unittest.main()
