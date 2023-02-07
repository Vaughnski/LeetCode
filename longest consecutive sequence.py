nums.sort()
last_num, curr_total, max_total = -1000000000000, 1, 1

if not nums: return 0;
if len(nums) == 1: return 1;

for num in nums:
    if num == (last_num + 1):
        curr_total += 1
    if num != last_num and num != (last_num + 1):
        curr_total = 1
    if curr_total > max_total:
        max_total = curr_total
    last_num = num
return max_total 