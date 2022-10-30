high = x //2
        low = 0
        if (x == 0 or x == 1):
            return x
        while low < high:
            mid = low + ((high- low) // 2)
            if mid * mid <= x and (mid+1) * (mid+1) > x:
                return mid
            elif((mid*mid) < x):
                low = mid+1
            else:
                high = mid -1
        return low