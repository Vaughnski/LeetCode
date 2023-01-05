class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        seen = set()
        for index, char in enumerate(s):
            if char not in seen:
                dict[char] = index
                seen.add(char)
            elif char in dict:
                del dict[char]
        return next(iter(dict.values()))  if dict else -1