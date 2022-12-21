class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        storage = {}
        counter = 0
        outList = []
        temp = ''
        for word in strs:
            temp = ''.join(sorted(word))
            if temp in storage:
                outList[storage[temp]].append(word)
            else:
                storage[temp] = counter
                outList.append([word])
                counter += 1
        return outList