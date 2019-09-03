class Solution(object):
    def spiralOrder(self, matrix):
        res = []
        if not matrix or not len(matrix):
            return res
        row,col = len(matrix),len(matrix[0])
        visited = [[0]*col for _ in range(row)]
        i,size = 0,row*col
        dx,dy=0,1
        while i<size:
            res.append(matrix[x][y])
            visited[x][y]=1
            if visited[(x+dx+row)%row][(y+dy+col)%col]:
                temp = -dx
                dx = dy
                dy = temp
            x+=dx
            y+=dy
            i+=1
        return res