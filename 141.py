from typing import Optional
from linked_list import ListNode, CycledLinkedList
import unittest


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True
        return False


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()

        self.assertEqual(
            solution.hasCycle(CycledLinkedList([3, 2, 0, -4], 1).head), True
        )
        self.assertEqual(solution.hasCycle(CycledLinkedList([1, 2], 0).head), True)
        self.assertEqual(solution.hasCycle(CycledLinkedList([1], -1).head), False)


unittest.main()
