from typing import Optional, List
from linked_list import ListNode, LinkedList
import unittest


class Solution:
    def toArray(self, root: 'Optional[Node]') -> List[int]:
        output = []
        while root:
            output.append(root.val)
            root = root.next

        return output






class TestSolution(unittest.TestCase):
    def runTest(self):
        solution = Solution()

        self.assertEqual(solution.toArray(LinkedList([1,2,3,4,3,2,1]).head), [1,2,3,4,3,2,1])


unittest.main()
