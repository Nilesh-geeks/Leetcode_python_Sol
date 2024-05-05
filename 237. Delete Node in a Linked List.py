Question ::237. Delete Node in a Linked List
Solved
Medium
Topics
Companies
There is a singly-linked list head and we want to delete a node node in it.

You are given the node to be deleted node. You will not be given access to the first node of head.

All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.

Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

The value of the given node should not exist in the linked list.
The number of nodes in the linked list should decrease by one.
All the values before node should be in the same order.
All the values after node should be in the same order.
Custom testing:

For the input, you should provide the entire linked list head and the node to be given node. node should not be the last node of the list and should be an actual node in the list.
We will build the linked list and pass the node to your function.
The output will be the entire list after calling your function.


Solution::
Intuition
    Simply copy the next val to current node val
Approach
    1. Copy the next value of the node to current node beacuse it 
       can't be the last node as it is mentoined in the problem.
    2. Run the loop till tail node is not found and copying the 
        value .
    3. delete the last Node
    4. Make last Node Next pointer to point NULL
Complexity
Time complexity:
    O(N)
Space complexity:
    O(1)
Code
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        while node.next.next!= None:
            node.next.val = node.next.next.val
            node = node.next
        node.next = None
     