"""
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes
(i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

Constraints:
The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            # save ptrs
            nxtPair = curr.next.next
            second = curr.next

            # reverse this pair
            second.next = curr
            curr.next = nxtPair
            prev.next = second

            # update ptrs
            prev = curr
            curr = nxtPair

        return dummy.next
