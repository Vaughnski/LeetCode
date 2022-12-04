class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        numOpen = n
        numClose = n
        self.para(numOpen,numClose, res, "")
        return res
    
    def para(self, numOpen, numClose, res, string):
        if numClose < numOpen:
            return
        if not numOpen and not numClose:
            res.append(string)
            return
        if numOpen:
            self.para(numOpen-1, numClose, res, string + '(')
        if numClose:
            self.para(numOpen, numClose-1, res, string + ')')