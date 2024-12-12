

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