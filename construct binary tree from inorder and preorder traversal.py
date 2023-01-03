if inorder:
            indy = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[indy])
            root.left = self.buildTree(preorder, inorder[0:indy])
            root.right = self.buildTree(preorder, inorder[indy+1:])
            return root