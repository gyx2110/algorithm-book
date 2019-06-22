class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        finished = [0 for _ in range(numCourses)]
        # 创建图的邻接表形式
        [graph[pair[0]].append(pair[1]) for pair in prerequisites]
        # 访问每个结点,只要有一个不能完成，则整体不能完成
        if min([self.dfs(graph,finished,i) for i in range(numCourses)]) == 0:
            return False
        return True
    def dfs(self, graph, finished, i):
        if finished[i] != 0:
            return finished[i]==1  
        # 标记当前结点正在访问
        finished[i] = -1
        # 访问所有依赖的课程结点
        for j in graph[i]:
            if not self.dfs(graph, finished, j):
                return False
        # 如果能到这一步，说明所有依赖的课程都能完成
        finished[i] = 1
        return True
if __name__ == "__main__":
    s = Solution()
    print s.canFinish(2, [[1,0],[0,1]])