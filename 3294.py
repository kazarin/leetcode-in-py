from linked_list import ListNode, LinkedList
from typing import Optional, List
import unittest


class Solution:
    def toArray(self, node: "Optional[ListNode]") -> List[int]:
        output = []
        current = node
        while current:
            output.append(current.val)
            current = current.next
        current = node.prev

        while current:
            output = [current.val] + output
            current = current.prev

        return output


class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()

        self.assertEqual(
            solution.toArray(LinkedList([1, 2, 3, 4, 5]).head), [1, 2, 3, 4, 5]
        )


unittest.main()
