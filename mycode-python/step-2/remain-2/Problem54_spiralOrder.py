class Solution(object):
    def spiralOrder(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        r, i, j, di, dj = [], 0, 0, 0, 1
        if matrix != []:
            for _ in range(row * col):
                r.append(matrix[i][j])
                matrix[i][j] = 0
                if matrix[(i + di) % row][(j + dj) % col] == 0:
                    di, dj = dj, -di
                i += di
                j += dj
        return r
if __name__ == "__main__":
    s = Solution()
    print s.spiralOrder([[0,2,3],[1,5,6],[7,8,9]])

# 0,2,3
# 0,5,6
# 7,8,9

# 0 2 3 6 9 8 7 0 5