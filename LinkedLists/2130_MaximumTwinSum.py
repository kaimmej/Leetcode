# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0

        # Make a second linked list that is a copy of the first.
        dummy = ListNode()
        dummyIterator = dummy
        curr = head
        while curr:
            # print(curr.val)
            newNode = ListNode(curr.val, None)
            dummyIterator.next = newNode
            dummyIterator = dummyIterator.next

            curr = curr.next


        # reverse the second linked list. 
        dummy = self.reverseList(dummy)


        # then, iterate through both of them at once. finding the maximum of the twinSums
        curr = head
        reverseCurr = dummy
        currentMax = 0
        while curr and reverseCurr:
            
            twinSum =  curr.val + reverseCurr.val

            currentMax = max(currentMax, twinSum)

            curr = curr.next
            reverseCurr = reverseCurr.next 


        return currentMax
    
    def reverseList(self, list: List[ListNode]) -> List[ListNode]:
        if not list:
            return None

        curr, prev = list, None
        while curr:
            tmpNext = curr.next
            curr.next = prev
            prev = curr
            curr = tmpNext


        # print(prev)
        return prev

        