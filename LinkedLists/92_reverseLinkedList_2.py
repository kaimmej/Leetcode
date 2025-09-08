# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head


        # Step 1) Find the left position in the list.
        # if position == left:
        #     pre = pre.next
        print("entering pre loop")
        dummy = ListNode(0, head)
        leftPrev, curr = dummy, head

        for _ in range(left - 1):
            leftPrev, curr = curr, curr.next
            print(_)

        prev = None
        # Step 2) Reverse the nodes between left and right. 
        # part of the list is reversed... 
        # We could start by reversing what is between left (INT), and right (INT)...
        for i in range(right-left+1):
            print(i)
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp

            
        # Step 3) fix the pointers at the start and the end of what we reversed... 

        # new start of reversed list
        # What will curr be at the end of hte loop? 
        leftPrev.next.next = curr

        # new end of reversed list
        leftPrev.next = prev

        return dummy.next