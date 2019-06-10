#dp[i][j]表示以matrix[i][j]结尾的最长递增长度
class Solution(object):
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        lst = []
        for i in range(m):
            for j in range(n):
                lst.append((matrix[i][j], i, j))
        #以值的大小进行排序,不排不行，必须保证依赖的子问题先求解
        lst.sort()
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for num, i, j in lst:
            dp[i][j] = 1
            #四个方向尝试
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                r, c = i + di, j + dj
                if 0 <= r < m and 0 <= c < n:
                    #如果小于当前点，则可以更新长度
                    if matrix[i][j] > matrix[r][c]:
                        dp[i][j] = max(dp[i][j], 1 + dp[r][c])
        return max([dp[i][j] for i in range(m) for j in range(n)])
if __name__ == "__main__":
    s = Solution()
    print s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])
    # print s.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]])