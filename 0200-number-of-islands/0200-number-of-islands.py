class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(grid, i, j):
            
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return

            if grid[i][j] == "0" or (i, j) in visited:
                return

            visited.add((i,j))

            dfs(grid, i-1, j)
            dfs(grid, i+1, j)
            dfs(grid, i, j-1)
            dfs(grid, i, j+1)





        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0
    
        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == "1" and (i, j) not in visited:
                    islands += 1
                    dfs(grid, i, j)
        return islands
                


