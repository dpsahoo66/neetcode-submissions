class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        
        # Directions for moving up, down, left, right
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # DFS function to mark reachable cells from ocean
        def dfs(r, c, visited):
            visited.add((r, c))  # Mark current cell visited
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Check bounds, if neighbor is not visited and height is >= current cell height (water can flow up)
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)
        
        pacific_reachable = set()
        atlantic_reachable = set()
        
        # Start DFS from Pacific borders (top row and left column)
        for i in range(m):
            dfs(i, 0, pacific_reachable)
        for j in range(n):
            dfs(0, j, pacific_reachable)
        
        # Start DFS from Atlantic borders (bottom row and right column)
        for i in range(m):
            dfs(i, n - 1, atlantic_reachable)
        for j in range(n):
            dfs(m - 1, j, atlantic_reachable)
        
        # Intersection of cells reachable by both oceans
        result = list(pacific_reachable.intersection(atlantic_reachable))
        return [list(cell) for cell in result]
