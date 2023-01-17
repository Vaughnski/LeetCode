def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root: return []
    prev_level, queue, out, zz = [], deque([root]), [], 1
    while queue:
        prev_level = []
        for _ in range(len(queue)):
            x = queue.popleft()
            prev_level.append(x.val)
            if x.left: queue.append(x.left)
            if x.right: queue.append(x.right)
        out.append(prev_level[::zz])
        zz *= (-1)
    return out