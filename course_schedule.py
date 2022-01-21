class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        adj = self.adjacencyList(numCourses, prerequisites)
        print(adj)

    def adjacencyList(self, n, edgesList):
        adjL = [ [] for _ in range(n)]
        
        for c1, c2 in edgesList:
            adjL[c2].append(c1)
        return adjL



p = Solution()
p.canFinish(2,[[1,0],[0,1]])