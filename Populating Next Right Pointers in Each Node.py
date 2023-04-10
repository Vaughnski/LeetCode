if not root: return;
queue = [root]
while queue:
    curr_level = queue.pop(0)
    if curr_level.left and curr_level.right:
        curr_level.left.next = curr_level.right
        if curr_level.next:
            curr_level.right.next = curr_level.next.left
        queue.append(curr_level.left)
        queue.append(curr_level.right)
return root