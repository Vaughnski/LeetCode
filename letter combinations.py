def letterCombinations(self, digits: str) -> List[str]:
    if len(digits) == 0:
        return []
    mp = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    out, index, path = [], 0, ''
    self.dfs(digits, mp, index, path, out)
    return out


def dfs(self, nums, mp, index, path, out):
    if index >= len(nums):
        out.append(path)
        return
    curr_word = mp[nums[index]]
    for i in curr_word:
        self.dfs(nums, mp, index + 1, path + i, out)