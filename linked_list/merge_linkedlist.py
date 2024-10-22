# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1 
        
        dummy = ListNode()
        head = dummy  # This is the current node in the merged list
        while(list1 is not None and list2 is not None):
            if (list1.val <= list2.val):
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next

        if list1 is not None:
            head.next = list1
        else:
            head.next = list2

        return dummy.next