low = bisect.bisect_left(nums, target)
return [low, bisect.bisect(nums,target)-1] if target in nums[low:low+1] else [-1,-1]