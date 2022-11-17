curr, next, prev = head, None, None
while curr is not None:
	next = curr.next
	curr.next = prev
	prev = curr
	curr = next
head = prev
return head