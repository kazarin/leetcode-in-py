from linked_list import ListNode, LinkedList
from typing import Optional
import unittest


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        prev_node = dummy

        while head and head.next:
            first_node = head
            second_node = head.next
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            prev_node = first_node
            head = first_node.next

        return dummy.next


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()

        self.assertEqual(
            solution.swapPairs(LinkedList([1, 2, 3, 4, 5]).head),
            LinkedList([2, 1, 4, 3, 5]),
        )


unittest.main()
