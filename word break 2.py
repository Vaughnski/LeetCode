class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        return self.helper(s,wordDict,'', [])


    def helper(self, remain, wordDicts, temp, res):
        if len(remain) == 0 and temp:
            if temp.strip() not in res:
                res.append(temp.strip())


        for s in range(len(remain)):
            for w in wordDicts:
                if w == remain[s - (len(w) - 1):s + 1] and (len(w)-1) == s:
                    self.helper(remain[s + 1:], wordDicts, temp + ' ' + w, res)

        return res