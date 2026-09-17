# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head
        prev= head 
        curr = head.next
        head = curr
        while True:
            next =curr.next
            curr.next = prev
            if not next or not next.next:
                prev.next =next
                break
            prev.next =next.next
            prev = next
            curr = prev.next
        return head
            

        

        
                
        
        