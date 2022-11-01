res = []
        curr = root
        stack = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left 
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res