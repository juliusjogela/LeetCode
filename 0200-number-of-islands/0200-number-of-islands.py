class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(i, j):
            if (i < 0 or i >= rows or j < 0 or j >= cols or 
                grid[i][j] == "0" or (i, j) in visited):
                return

            visited.add((i, j))
            dfs(i-1, j)  # up
            dfs(i+1, j)  # down
            dfs(i, j-1)  # left
            dfs(i, j+1)  # right
        
        cols = len(grid[0])
        rows = len(grid)
        visited = set()
        islands = 0
        for i in range(rows):
            for j in range(cols):
                
                if grid[i][j] == "1" and (i, j) not in visited:
                    islands += 1
                    dfs(i, j)

        return islands

