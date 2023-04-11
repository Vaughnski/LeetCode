left, right, max_a, curr_a = 0, len(height) - 1, 0, 0
while left < right:
    curr_a = min(height[left], height[right]) * (right - left)
    max_a = max(max_a, curr_a)
    if height[left] > height[right]:
        right -= 1
    else:
        left += 1
return max_a