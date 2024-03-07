Question :: 876. Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
Solution::

Complexity::

Time complexity:
O(N) 

Space complexity:
O(1)

Code::
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while  fast!= None and  fast.next!=None:
            fast = fast.next.next
            slow = slow.next
        return slow

        



        