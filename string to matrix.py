import re
import numpy as np
string = 'name,5,name2,6:l1;name,8,name2,9:l2'
columns_total = string.count(':') + 1
rows_total = (string.count(',') // columns_total) + 1
y_count, x_count, row, matrix = 1, 1, 1, np.zeros(shape=(rows_total, columns_total) , dtype=np.dtype('U100'))
split = re.split(r',|;', string)
for index, value in enumerate(split):
    if index % 2 == 0 and value not in matrix[:, 0]:
        matrix[y_count][0] = value
        y_count += 1
    if index %2 ==1:
        colon_check = value.find(':')
        if colon_check == -1:
            matrix[row][x_count] = value
            row+=1
        else:
            matrix[0][x_count] = value[(colon_check + 1):]
            matrix[row][x_count] = value[:colon_check]
            x_count += 1
            row = 1