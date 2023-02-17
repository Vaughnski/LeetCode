ops = {'+' : lambda x,y: y+x, '-' : lambda x,y: y-x, '*' : lambda x,y: x*y, '/' : lambda x,y: y/x}
        stack = []
        temp = 0
        for token in tokens:
            if token in ops:
                temp = ops[token](int(stack.pop()), int(stack.pop()))
                stack.append(temp)
            else:
                stack.append(token)
        return int(stack.pop())