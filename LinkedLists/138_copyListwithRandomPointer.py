"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        

        # Start by just printing the nodes.
        # input: [[7,null],[13,0],[11,4],[10,2],[1,0]]
        copyNodeDirectory = { None : None }


        # First time through we create a newNode "copy" and store it in the hashMap
        curr = head
        while curr: 
            newNode = Node(curr.val)
            copyNodeDirectory[curr] = newNode
            curr = curr.next

        curr = head
        while curr:
            newNode = copyNodeDirectory[curr]
            newNode.next = copyNodeDirectory[curr.next]
            newNode.random = copyNodeDirectory[curr.random]
            curr = curr.next


        # return the head of the copied linked list
        return copyNodeDirectory[head]