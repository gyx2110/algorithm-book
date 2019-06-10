class Solution(object):
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    @classmethod
    def numIslands(self, grid):
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.bfs(grid,i,j)
                    ans +=1
        return ans
    @classmethod
    def bfs(self,grid,i,j):
        grid[i][j] = '.'
        for k in range(4):
            m = i+self.dx[k]
            n = j+self.dy[k]
            if m>-1 and m<len(grid) and n >-1 and n<len(grid[0]) and grid[m][n] == '1':
                self.bfs(grid,m,n)
        return
if __name__ == "__main__":
    print Solution.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])