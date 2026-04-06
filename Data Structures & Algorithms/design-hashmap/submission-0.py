class ListNode:
    def __init__(self, key:int = -1, val:int = -1, nxt = None):
        self.key = key
        self.val = val
        self.next = nxt

class MyHashMap:

    def __init__(self):
        self.cache = [ListNode()] * ((10**3) + 1) 

    def put(self, key: int, value: int) -> None:
        curr = self.cache[key % (10**3)]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        curr = self.cache[key % (10**3)]
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1


    def remove(self, key: int) -> None:
        curr = self.cache[key % (10**3)]
        while curr.next and curr.next.key != key:
            curr = curr.next
        if not curr.next:
            return
        curr.next = curr.next.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)