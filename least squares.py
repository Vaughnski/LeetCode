if n<2:
            return n 
        squares = []
        i = 1
        while i * i <= n:
            squares.append( i * i )
            i += 1
        counter = 0
        checker = {n}
        while checker:
            counter += 1 
            temp = set()
            for x in checker:
                for y in squares:
                    if x == y:
                        return counter
                    if x < y:
                        break
                    temp.add(x-y)
            checker = temp 
        return counter