

def main():
    # Create a linked list
    head = ListNode(0)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4


    linkNodes(node1, node2)
    linkNodes(node2, node3)
    linkNodes(node3, node4)

    # Print the linked list
    printList(head)


    # 
    # DELETE A NODE
    #   This is called chaining next pointers together.
    head.next = head.next.next

    # Print the linked list
    printList(head)


# WORKING WITH DUMMY NODES....
# WHY? Dummy nodes give us flexibility in our code.
    #   They help us avoid edge cases and make our code cleaner.
    #   They also help us avoid null pointer exceptions
    
    # TWO WAYS TO MAKE A LIST NODE
    dummy = ListNode()
    dummy = ListNode(0, head)

    dummy = dummy.next
    # return dummy

# REVERSE A LINKED LIST
    prev = None
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp


## USING FAST AND SLOW POINTERS 
#   This is called the Floyd's Tortoise and Hare algorithm.
    # Find the middle of the list using Slow and Fast pointers 
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next










# Creating a linked list
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# Link two nodes 
def linkNodes(node1, node2):
    node1.next = node2
    return node1

def printList(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print("NULL")

def TraverseList(node):
    curr = node
    while curr:
        print("Current Val: ", curr.val)
        node = node.next




main()