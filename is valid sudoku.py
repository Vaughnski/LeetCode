dict = collections.defaultdict(list)
for x in range(9):
    for y in range(9):
        char = board[x][y]
        if char != ".":
            if char in dict:
                for position in dict[char]:
                    if (position[0] == x) or  (position[1] == y) or (position[0]//3 == x//3 and position[1]//3 == y//3):
                        return False
            dict[char].append((x,y))
return True