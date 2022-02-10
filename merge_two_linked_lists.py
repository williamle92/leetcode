from typing import List
import unittest
''''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    # First we are going to create 2 pointers that points to the head of our newly create listNode class
    # listnode can take any value since we are going to return the head.next
    # current is going to traverse the linked list while the dummy points to the head, we need a dummy or else we
    # we can not traverse the linkedlist from the beginning again
    curr = dummy = ListNode(0)

    # Check to see if there is both a l1 and l2
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    # since dummy has always been pointing to the head of the linked list, we can call dummy.next 
    return dummy.next

