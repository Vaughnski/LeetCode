class Codec:
    def serialize(self, root):
        def recur(node):
            if node:
                vals.append(str(node.val))
                recur(node.left)
                recur(node.right)
            else:
                vals.append('#')
        vals = []
        recur(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def complete():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = complete()
            node.right = complete()
            return node
        vals = iter(data.split())
        return complete()
