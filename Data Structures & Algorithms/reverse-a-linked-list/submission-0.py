# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur, prev = head, None

        while cur:
            nxt = cur.next  #save the pointer info before link is broken
            cur.next = prev    #current now is pointing to the next element
            prev = cur         # move prev to current now
            cur = nxt          # saved pointer info assigned
        return prev             # prev pointer now is at head


