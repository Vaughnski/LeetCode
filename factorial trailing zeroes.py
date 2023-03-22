res,num = 0, 1
while n>0:
    num*=n
    n-=1
num = str(num)
for char in reversed(num):
    if char == '0':
        res+=1
    else:
        return res