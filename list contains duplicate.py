if (len(nums) == 1): return False 
nums.sort()
for num in range(0, (len(nums)-1)):
	if (nums[num] == nums[num+1]):
		return True
return False