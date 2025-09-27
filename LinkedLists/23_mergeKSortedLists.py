# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # Choose the first two lists and merge them. Then keep doing this until you run out of lists.... 
        if not lists or len(lists) == 0:
            return None


        while len(lists) > 1:
            mergedLists = []
            lenLists = len(lists)
            print(f" {lenLists=}")
            # we merge two lists at a time
            for i in range(0, lenLists, 2):
                print(f"   {i}")
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < lenLists else None
                mergedLists.append(self.mergeTwoLists(l1,l2))
            lists = mergedLists
        
        return lists[0]


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = node = ListNode()

            while list1 and list2:
                if list1.val < list2.val:
                    node.next = list1
                    list1 = list1.next
                else:
                    node.next = list2
                    list2 = list2.next
                node = node.next

            node.next = list1 or list2

            return dummy.next        
    


    def mergeLists(self, l1: List[ListNode], l2: List[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode()

        while l1 and l2:
            if l1.val < l2.val:
                newNode = ListNode(l1.val)
                curr.next = newNode
            else:
                newNode = ListNode(l2.val)
                curr.next = newNode
            curr = curr.next
        
        curr.next = l1 or l2



        return dummy.next