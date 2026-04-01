class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class LinkedList:
    
    def __init__(self):
        self.head = ListNode()
        self.tail = self.head

    def get(self, index: int) -> int:
        node = self.head.next
        i = 0
        while node:
            if i == index:
                return node.val
            node = node.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        node = ListNode(val, self.head.next)
        self.head.next = node
        if self.tail == self.head:
            self.tail = self.head.next

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        node = self.head
        i = 0
        while i < index and node:
            i += 1
            node = node.next

        if node and node.next:
            if node.next == self.tail:
                node.next = None
                self.tail = node
            else:
                node.next = node.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        res = []
        node = self.head.next
        while node:
            res.append(node.val)
            node = node.next
        return res

