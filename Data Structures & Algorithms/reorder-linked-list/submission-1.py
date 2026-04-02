# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, reverseHead = None, slow.next
        slow.next = None

        while reverseHead:
            nxt = reverseHead.next
            reverseHead.next = prev
            prev = reverseHead
            reverseHead = nxt
        
        reverse = prev
        dummy = ListNode()
        newList = dummy
        curr = head
        
        while curr and reverse:
            newList.next = curr
            newList = newList.next
            curr = curr.next

            newList.next = reverse
            newList = newList.next
            reverse = reverse.next

        if curr:
            newList.next = curr
        elif reverse:
            newList.next = reverse


