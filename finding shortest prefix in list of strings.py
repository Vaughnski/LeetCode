shortest = min(strs, key = len)
for index, value in enumerate(shortest):
	for word in strs:
		if(word[index]!=value):
                    return(shortest[:index])
return shortest