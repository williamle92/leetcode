'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeNthFromEnd(head, n):
    # create a dummy node that is 1 before the actual head 
    dummy = ListNode(0, head)
    # Left is going to be where dummy is located
    left = dummy
    # Right will start at the head of the list
    right = head

    # Now we move right n times down the list
    while n >0 and right:
        right = right.next
        n -= 1

    # Now right right be n + 1 ahead of left (since we moved left back one since we are reassigning the left before the node to be removed)
    # now move to the end of the list where it is None
    while right:
        right = right.next
        left = left.next

    # now left is before the node we are trying to remove and right is at the end
    # we take the left currently and assign it to the next next node
    left.next = left.next.next

    # finally return the dummy.next