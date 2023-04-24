"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None: return None
        dct = {}
        curr= head
        while curr:
            dct[curr] = Node(curr.val, None, None)
            curr = curr.next
        curr = head
        while curr:
            if curr.next:
                dct[curr].next = dct[curr.next]
            if curr.random:
                dct[curr].random = dct[curr.random]
            curr = curr.next
        return dct[head]