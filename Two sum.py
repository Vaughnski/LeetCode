class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        processed = {}

        for index, value in enumerate(nums):
            difference = target - value

            if (difference in processed):
                return [processed[difference], index]

            processed[value] = index
