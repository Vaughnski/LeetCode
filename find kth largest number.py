d ={}
nums.sort(reverse = True)
count = 1
for num in nums:
	d[count] = num
	count+=1
return d[k]