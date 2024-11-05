class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_list(self):
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.next

        return result


class CycledLinkedList:
    def __init__(self, values, pos):
        self.head = LinkedList(values).head
        current = self.head
        loop = None
        if pos != -1:
            i = 0
            while current.next:
                if i == pos:
                    loop = current
                current = current.next
                i += 1
            current.next = loop


class LinkedList:
    def __init__(self, values):
        self.head = ListNode(values[0])
        current = self.head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next

        return result

    def __eq__(self, other):
        return self.to_list() == other.to_list()
