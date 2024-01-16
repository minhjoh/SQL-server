# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Check if linked list is empty or contains only one node
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even
    
        # Traverse the linked list in pairs of odd and even nodes
        while even and even.next:
            # Connect the next odd node with the current odd node
            odd.next = even.next
            odd = odd.next
            
            # Connect the next even node with the current even node
            even.next = odd.next
            even = even.next

        # Connect the last odd node with the head of even nodes
        odd.next = even_head
        return head
        

        

            
            