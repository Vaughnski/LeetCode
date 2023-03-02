class Solution:
    def calculate(self, s: str) -> int:
        def helper(sign, sub):
            if sign == '+': stack.append(sub);
            if sign == '-': stack.append(-sub);
            if sign == '*': stack.append(stack.pop() * sub);
            if sign == '/': stack.append(int(stack.pop() / sub));


        i, num, stack, sign = 0, 0, [], "+"

        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] in '+-*/':
                helper(sign, num)
                num, sign = 0, s[i]
            i += 1
        helper(sign, num)
        return sum(stack)
