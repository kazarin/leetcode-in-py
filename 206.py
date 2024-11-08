from linked_list import ListNode, LinkedList
from typing import Optional
import unittest


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()

        self.assertEqual(
            solution.reverseList(LinkedList([1, 2, 3, 4, 5]).head),
            LinkedList([5, 4, 3, 2, 1]),
        )


unittest.main()
