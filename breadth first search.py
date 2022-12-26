que, out = deque(), []

if root:
    que.append(root)
while que:
    level = []
    for _ in range(len(que)):
        x = que.popleft()
        level.append(x.val)
        if x.left:
            que.append(x.left)
        if x.right:
            que.append(x.right)
    out.append(level)
return out