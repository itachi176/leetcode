# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        #get second partion
        while(fast and fast.next):
            slow = slow.next 
            fast = fast.next.next

        second = slow.next
        slow.next = None # cut first partion 
        prev = None
        nextPtr = None
        #reverse second partion
        while (second):
            nextPtr = second.next
            second.next = prev 
            prev = second
            second = nextPtr 
        
        # merge
        second = prev
        first = head
        while(second):
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

