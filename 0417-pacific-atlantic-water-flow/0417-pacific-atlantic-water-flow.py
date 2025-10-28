class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        
        # Sets to track which cells can reach each ocean
        pacific = set()
        atlantic = set()

        def dfs(i, j, visited):
            visited.add((i, j))
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for di, dj in directions:
                checkI = i + di
                checkJ = j + dj

                if (0 <= checkI < m) and (0 <= checkJ < n) and (checkI, checkJ) not in visited and heights[checkI][checkJ] >= heights[i][j]:
                    dfs(checkI, checkJ, visited)



        for c in range(n):
            dfs(0, c, pacific)  # Top row
        for r in range(m):
            dfs(r, 0, pacific)  # Left column
        
        # Start DFS from Atlantic edges (bottom row and right column)
        for c in range(n):
            dfs(m - 1, c, atlantic)  # Bottom row
        for r in range(m):
            dfs(r, n - 1, atlantic)  # Right column
        
        # Find intersection - cells reachable from both oceans
        return list(pacific & atlantic)
                    
