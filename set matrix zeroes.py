#the col0 row0 thing is so that the matrix is updated in place

l_row, l_col, row0, col0 = len(matrix), len(matrix[0]), False, False

#iter thru the first col
for i in range(0, l_row):
    if matrix[i][0] == 0:
        col0 = True

#iter thru the first row
for j in range(0, l_col):
    if matrix[0][j] == 0:
        row0 = True

#iter thru the 1 => rest of matrix, to set the col and row headers to 0
for i in range(1, l_row, 1):
    for j in range (1, l_col, 1):
        if matrix[i][j] ==0:
            matrix[i][0], matrix[0][j] = 0, 0

#iter thru the 1 => rest of matrix, to set the individ [i][j] cells to 0 if the row or col header = 0
for i in range(1, l_row, 1):
    for j in range (1, l_col, 1):
        if matrix[i][0] ==0 or matrix[0][j] ==0:
            matrix[i][j] = 0

#return to col 0, updating all cols with 0s
if col0 == True:
    for i in range(0, l_row):
        matrix[i][0] = 0

#return to row 0, updating all rows with 0s
if row0 == True:
    for j in range(0, l_col):
        matrix[0][j] = 0