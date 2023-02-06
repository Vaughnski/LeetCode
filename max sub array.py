if len(nums) == 1: return nums[0];
        n = len(nums)
        cur_sum = 0
        max_sum = -10001
        for ind in range(0,n):
            cur_sum = cur_sum + nums[ind]
            if cur_sum > max_sum:
                max_sum = cur_sum
            if cur_sum < 0:
                cur_sum = 0
        return max_sum