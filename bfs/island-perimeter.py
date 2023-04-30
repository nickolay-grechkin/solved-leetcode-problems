from collections import deque

def islandPerimeter(grid):
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            perimeter = 0
            while q:
                row, col = q.popleft()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (r not in range(rows) or c not in range(cols) or grid[r][c] == 0):
                        perimeter+=1
                    elif (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))
            return perimeter


        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == 1 and (r, c) not in visited):
                    return bfs(r, c)

print(islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))