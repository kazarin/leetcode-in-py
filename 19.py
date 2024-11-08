from linked_list import ListNode, LinkedList
from typing import Optional
import unittest


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head.next
        for i in range(0, n):
            if fast is None:
                return slow.next
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()

        self.assertEqual(
            solution.removeNthFromEnd(LinkedList([1, 2, 3, 4, 5]).head, 2),
            LinkedList([1, 2, 3, 5]),
        )
        self.assertEqual(solution.removeNthFromEnd(LinkedList([1]).head, 1), None)
        self.assertEqual(
            solution.removeNthFromEnd(LinkedList([1, 2]).head, 2), LinkedList([2])
        )


unittest.main()
