from config import *
from Models.cell import *
from Models.node import *
from Algorithms.helper import *


def dfs(draw, grid, start, end):
    stack = [Node(start, [start])]
    visited = set()

    while stack:
        current_node = stack.pop()
        current_cell = current_node.cell

        if current_cell in visited:
            continue

        visited.add(current_cell)

        # تلوين الخلايا اللي بنزورها
        if current_cell != start and current_cell != end:
            current_cell.make_visited()

        if current_cell == end:
            for c in current_node.path:
                if c != start and c != end:
                    c.make_path()
                draw()
            return True

        for neighbor in get_neighbors(grid, current_cell):
            if neighbor not in visited:
                stack.append(
                    Node(neighbor, current_node.path + [neighbor])
                )

        draw()

    return False

