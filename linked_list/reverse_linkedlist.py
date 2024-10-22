# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        prev = None 
        nextPtr = None 
        while (head != None):
            nextPtr = head.next
            head.next = prev 
            prev = head
            head = nextPtr

        return prev
        