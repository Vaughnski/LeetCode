for index in range(len(digits) -1, -1, -1):
	if (digits[index] == 9):
        	digits[index] = 0
	else:
                digits[index] += 1
                return digits
digits.insert(0, 1)
return digits