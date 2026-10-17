# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode() #dummy never moves forward, its always point to the start
        tail = dummy        #initialised at the start

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next        # move the list1's pointer forward
            else:
                tail.next = list2
                list2 = list2.next        # move the list1's pointer forward
            tail = tail.next     #move tail from dummy node to added node

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next

