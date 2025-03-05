class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        island_count = 0

        # DFS function to mark the connected '1's as visited
        def dfs(i, j):
            # Base case: if out of bounds or water ('0'), return
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0':
                return
            # Mark the current land as visited
            grid[i][j] = '0'
            # Explore the four possible directions (up, down, left, right)
            dfs(i + 1, j)  # Down
            dfs(i - 1, j)  # Up
            dfs(i, j + 1)  # Right
            dfs(i, j - 1)  # Left

        # Iterate through the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':  # Found a new island
                    island_count += 1
                    dfs(i, j)  # Explore the entire island

        return island_count
