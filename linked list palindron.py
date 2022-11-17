list = []
while head:
	list.append(head.val)
	head = head.next
return list == list[::-1]