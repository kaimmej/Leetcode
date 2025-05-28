# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
       # I need a carry.
        carry = 0
        head = l1
        tail = l1

        # I need a loop to go over the numbers. 
        while l1 or l2:
            if l1 is None:
                tail.next = ListNode(0)  # Create a new node
                tail = tail.next  # Update the tail
                l1 = tail  # Update l1
                sum = l2.val + carry
            elif l2 is None:
                sum = l1.val + carry
            else:
                sum = l1.val + l2.val + carry

            if sum >= 10:
                carry = 1
                l1.val = sum % 10
            else:
                carry = 0
                l1.val = sum

            # I need to update l1 to the next node.
            if l1 is not None:
                if l1.next == None:
                    tail = l1
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if carry:
            newNode = ListNode(1)
            tail.next = newNode

        return head


# SOLUTION 2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        cur = dummy

        # Creating remainder outside the loop so it is still active to be checked after the While loop exits.
        remainder = 0

        # Go through, add the numbers together and create a new Node. 
        while l1 or l2: 
            sumNode = ListNode()
            cur.next = sumNode
            val1 = 0
            val2 = 0
            if l1:
                val1 = l1.val
            if l2:
                val2 = l2.val
            sum = val1 + val2 + remainder
            if remainder != 0:
                remainder = 0

            if sum >= 10:
                print(sum)
                remainder = 1
                sum = sum % 10
            sumNode.val = sum

            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next




        if remainder == 1: 
            sumNode = ListNode(1)
            cur.next = sumNode
            remainder = 0

        
        return dummy.next