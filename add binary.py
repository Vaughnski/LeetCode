a= list(a)
        b= list(b)
        res = ""
        carry = 0
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            res += str(carry % 2)
            carry //= 2 
        return res[::-1]