if not root.left and not root.right:
            return True
        
        stack = [[root.left, root.right]]
        
        
        while stack:
            pair = stack.pop()
            left, right = pair[0], pair[1]
             
            if left is None and right is None:
                continue 
                
            if left is None or right is None:
                return False 
            
            if left.val == right.val:
                stack.insert(0, [left.left, right.right])
            
                stack.insert(0, [left.right, right.left])
            
            else:
                return False
                
        return True 
                
              