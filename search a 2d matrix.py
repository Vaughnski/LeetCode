rows, row_elim = len(matrix), len(matrix)
for row in range(0, len(matrix)):
    if target == matrix[row][0]:
        return True
    if target < matrix[row][0]:
        row_elim = row
        break

for i in range(0,rows):
    if target in matrix[i]:
        return True

return False