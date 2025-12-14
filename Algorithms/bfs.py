from collections import deque
from config import *
from Models.cell import *
from Models.node import *

# --- Get neighbors in 4 directions
def get_neighbors(grid, cell):
    neighbors = []
    for d in [(-1,0),(1,0),(0,-1),(0,1)]:
        r, c = cell.row + d[0], cell.col + d[1]
        if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c].color != "black":
            neighbors.append(grid[r][c])
    return neighbors

# --- BFS Algorithm
def bfs(draw, grid, start, end):
    queue = deque()
    start_node = Node(start, [start])
    queue.append(start_node)
    
    visited = set()
    visited.add((start.row, start.col))

    while queue:
        current_node = queue.popleft()  
        current_cell = current_node.cell

        if current_cell != start and current_cell != end:
            current_cell.make_visited()
        draw()

        # Check if we reached the goal
        if current_cell == end:
            for c in current_node.path:
                if c != start and c != end:
                    c.make_path()
                draw()
            return True

        # Explore neighbors
        for neighbor in get_neighbors(grid, current_cell):
            neighbor_pos = (neighbor.row, neighbor.col)
            if neighbor_pos not in visited:
                visited.add(neighbor_pos)
                new_path = current_node.path + [neighbor]
                queue.append(Node(neighbor, new_path))

    return False