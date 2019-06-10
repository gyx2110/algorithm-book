class Solution(object):
    def minPathSum(self, grid):
        size = len(grid)
        if grid == None or size==0:
            return 0
        dp = [[0]*len(grid[0]) for _ in range(size)]
        
        //Base Case
        dp[0][0] = grid[0][0]
        for i in range(1,size):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1,len(grid[0])):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        //一般情况
        for i in range(1,size):
            for j in range(1,len(grid[0])):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[-1][-1]
if __name__ == "__main__":
    s = Solution()
    print s.minPathSum([[1,3,5,9],[8,1,3,4],[5,0,6,1],[8,8,4,0]])