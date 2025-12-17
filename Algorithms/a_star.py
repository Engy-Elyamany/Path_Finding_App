import time
from queue import PriorityQueue
from config import *
from Models.cell import *
from Models.node import *
from Algorithms.helper import get_neighbors

# --- Heuristic for grid (Manhattan distance)
def heuristic(cell):
    return abs(cell.row - end_cell.row) + abs(cell.col - end_cell.col)

def a_star(draw, grid, start, end):
    global end_cell
    end_cell = end
    count = 0  # random tie-breaker for PriorityQueue
    start_time = time.perf_counter()
    expanded_nodes = 0

    from queue import PriorityQueue
    q = PriorityQueue()
    start_node = Node(cell=start, path=[start])
    
    q.put((heuristic(start),0,count,start_node))  # initial f,g,count,node

    while not q.empty():
        h, g, _, node = q.get()
        expanded_nodes += 1
        current_cell = node.cell

        if current_cell == end:
            for cell in node.path:
                if cell != start and cell != end:
                    cell.make_path()
                    draw()
            end_time = time.perf_counter()
            return {
                "found": True,
                "time_ms": (end_time - start_time) * 1000,
                "expanded_nodes": expanded_nodes,
                "path_length": len(node.path)
            }

        neighbors = get_neighbors(grid, current_cell)
        for n in neighbors:
            if n not in node.path:
                if n != start and n != end:
                    n.make_visited()
                count += 1
                neighbor_path = node.path + [n]
                neighbor = Node(n, neighbor_path)
                new_g = g + 1
                h_new = new_g + heuristic(n)
                q.put((h_new, new_g, count, neighbor))
        draw()

    end_time = time.perf_counter()
    return {
        "found": False,
        "time_ms": (end_time - start_time) * 1000,
        "expanded_nodes": expanded_nodes,
        "path_length": 0
    }
