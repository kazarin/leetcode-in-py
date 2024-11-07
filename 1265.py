from linked_list import ListNode, LinkedList
from io import StringIO
import unittest
from unittest.mock import patch


class ImmutableListNode(ListNode):
    pass


def getNext(self) -> "ImmutableListNode":
    return self.next


def printValue(self) -> None:
    print(self.val)


ListNode.getNext = getNext
ListNode.printValue = printValue


class Solution:
    def printLinkedListInReverse(self, head: "ImmutableListNode") -> None:
        if head is None:
            return
        self.printLinkedListInReverse(head.getNext())
        head.printValue()


class TestSolution(unittest.TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def runTest(self, mock_stdout):
        solution = Solution()
        solution.printLinkedListInReverse(LinkedList([1, 2, 3, 4]).head)

        self.assertEqual(
            list(map(int, mock_stdout.getvalue().strip().split("\n"))), [4, 3, 2, 1]
        )


unittest.main()
