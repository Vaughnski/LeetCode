class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # cut the list into two halves
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(second)
        return self.merge(l, r)

    #3 pointers to move along the left right and returned LL
    def merge(self, l, r):
        #base case of no l or r
        if l is None:
            return r
        elif r is None:
            return l

        #keeping starter as "head" to return
        start = ListNode(0)

        #this var is populating the linked list that is returned
        point = start
        while l and r:
            
            #compare the l and r, moving the l and r pointers along
            if l.val <= r.val:
                point.next = l
                l = l.next
            else:
                point.next = r
                r = r.next
                
            #move returned pointer along
            point = point.next
        
        #l or r is Null so populating the remaining list with non Null l or r 
        point.next = l if r is None else r
        return start.next