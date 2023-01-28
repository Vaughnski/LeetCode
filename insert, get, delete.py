import random 

class RandomizedSet:

    def __init__(self):
        self.nums, self.dict = [], {}

    def insert(self, val: int) -> bool:
        if val not in self.nums:
            self.nums.append(val)
            self.dict[val] = (len(self.nums) - 1)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.nums:
            idx, num = self.dict[val], self.nums[-1]
            self.nums[idx], self.dict[num] = num, idx
            self.nums.pop(); del self.dict[val] 
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.nums)