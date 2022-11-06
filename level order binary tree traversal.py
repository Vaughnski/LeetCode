if not root:
            return 0  
        stack, level = [root], 0
        
        while stack:
            next_level = []
            while stack:
                pop = stack.pop()
                if pop.left:
                    next_level.append(pop.left)
                if pop.right:
                    next_level.append(pop.right)
            stack = next_level
            level += 1
        return level