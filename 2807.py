from linked_list import ListNode, LinkedList
from typing import Optional
import unittest
import math


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        current = head
        while current and current.next:
            tmp = current.next
            new_node = ListNode(math.gcd(current.val, current.next.val))
            new_node.next = tmp
            current.next = new_node
            current = tmp

        return head


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()

        self.assertEqual(
            solution.insertGreatestCommonDivisors(LinkedList([18, 6, 10, 3]).head),
            LinkedList([18, 6, 6, 2, 10, 1, 3]),
        )


unittest.main()
