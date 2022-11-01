res = []
        def traverse(root):
            if not root:
                return root
            traverse(root.left)
            res.append(root.val)
            traverse(root.right)
        traverse(root)
        return res