# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        curr = head
        while curr:
            if curr.val == None:
                return True
            curr.val = None
            curr = curr.next
        
        return False
    





class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        
        return False
# Explain this solution below:
# The solution uses the Floyd's Tortoise and Hare algorithm to detect a cycle in a linked list.
# It uses two pointers, slow and fast. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time.
# If there is a cycle, the fast pointer will eventually meet the slow pointer. If there is no cycle, the fast pointer will reach the end of the list.
# The time complexity of this solution is O(n), where n is the number of nodes in the linked list. This is because each pointer traverses the list at most once.
# The space complexity is O(1) because we are using only two pointers and not using any additional data structures.