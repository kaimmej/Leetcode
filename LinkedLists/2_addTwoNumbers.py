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
        