"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list 
that has Node.val == val, and return the new head.

Example 1:

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class Solution:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = ListNode(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        current = self.head
        while(current):
            if current.data == val:
                print(current.data)
                current = current.next

    def printResult(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next


result = Solution()
result.insert(1)
result.insert(2)
result.insert(6)
result.insert(3)
result.insert(4)
result.insert(5)
result.insert(6)
result.printResult()
result.removeElements(val=6)
