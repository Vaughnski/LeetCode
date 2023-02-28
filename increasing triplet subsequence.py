low = mid = sys.maxsize
for num in nums:
    if num <= low:
        low = num
    elif num <= mid:
        mid = num
    else:
        return True
return False