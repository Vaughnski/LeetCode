s = columnTitle[::-1] 
return sum((ord(s[char])-64)* (26 ** char) for char in range(0, len(s)))