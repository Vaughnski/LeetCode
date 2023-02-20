row_len, col_len = len(matrix), len(matrix[0])

        out, top, left, bottom, right = [], 0, 0, len(matrix)-1, len(matrix[0])-1
        while(top <= bottom and right >= left):
            for top_ind in range(left, right+1):
                out.append(matrix[top][top_ind])
            top += 1
            for right_ind in range(top, bottom+1):
                out.append(matrix[right_ind][right])
            right -= 1
            for bottom_ind in range(right, left-1, -1):
                out.append(matrix[bottom][bottom_ind])
            bottom -= 1
            for left_ind in range(bottom, top-1, -1):
                out.append(matrix[left_ind][left])
            left += 1
        return out[:row_len*col_len]