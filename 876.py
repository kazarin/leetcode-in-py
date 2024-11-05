from typing import Optional
from linked_list import ListNode, LinkedList
import unittest


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()
        self.assertEqual(
            solution.middleNode(LinkedList([1, 2, 3, 4, 5]).head), LinkedList([3, 4, 5])
        )


unittest.main()
