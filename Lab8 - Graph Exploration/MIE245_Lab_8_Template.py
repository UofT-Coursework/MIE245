from typing import List


def count_fire_zones(grid: List[List[int]]) -> int:
    """
    Forest Fire Zones (Graph Exploration)

    Counts the number of connected fire zones in a grid.

    Input:
        grid: R x C grid of integers (0 or 1)

    Output:
        Number of distinct fire zones (int)
    """
    # Create visited set, fire zone counter, and reusable stack
    visited = set()
    fire_zones = 0
    zone = [] # stack - not queue, because then pop(0) is O(n) in python

    # Iterate over all elements in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If an unvisited fire is found, perform DFS
            if grid[i][j] == 1 and (i, j) not in visited:
                visited.add((i, j)) # Add to visited
                zone.append((i, j)) # Add to zone stack

                # DFS
                while zone:
                    x, y = zone.pop() # pop from stack, O(1)
                    # Check all neighbors
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        # Make sure neighbor is in bounds
                        # (in length) and (in height) and (is fire) and (not visited)
                        if (0 <= nx < len(grid)) and (0 <= ny < len(grid[0])) and (grid[nx][ny] == 1) and ((nx, ny) not in visited):
                            visited.add((nx, ny))
                            zone.append((nx, ny))
                fire_zones += 1
    return fire_zones

# RECURSIVE DFS
def count_fire_zones(grid: List[List[int]]) -> int:
    """
    Forest Fire Zones (Graph Exploration)

    Counts the number of connected fire zones in a grid.

    Input:
        grid: R x C grid of integers (0 or 1)

    Output:
        Number of distinct fire zones (int)
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
            return
        grid[r][c] = 0  # mark as visited
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                count += 1
                dfs(r, c)

    return count