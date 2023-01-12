red = 0
white = 0
blue = len(nums) -1
while blue >= white:
    if nums[white] == 0:
        nums[red], nums[white] = nums[white], nums[red]
        red += 1
        white += 1
    elif nums[white] == 1:
        white+=1
    else:
        nums[blue], nums[white] = nums[white], nums[blue]
        blue -= 1 
