import time
from config import *
from Models.cell import *
from Models.node import *
from Algorithms.helper import *


def dfs(draw, grid, start, end):
    start_time = time.perf_counter()
    expanded_nodes = 0

    stack = [Node(start, [start])]
    visited = set()

    while stack:
        current_node = stack.pop()
        expanded_nodes += 1  # كل Node بنطلعه من الـ stack يعتبر Expanded Node

        current_cell = current_node.cell

        if current_cell in visited:
            continue

        visited.add(current_cell)

        # الرسم زي ما هو
        if current_cell != start and current_cell != end:
            current_cell.make_visited()

        if current_cell == end:
            for c in current_node.path:
                if c != start and c != end:
                    c.make_path()
                draw()

            end_time = time.perf_counter()
            return {
                "found": True,
                "time_ms": (end_time - start_time) * 1000,
                "expanded_nodes": expanded_nodes,
                "path_length": len(current_node.path)
            }

        for neighbor in get_neighbors(grid, current_cell):
            if neighbor not in visited:
                stack.append(Node(neighbor, current_node.path + [neighbor]))

        draw()

    end_time = time.perf_counter()
    return {
        "found": False,
        "time_ms": (end_time - start_time) * 1000,
        "expanded_nodes": expanded_nodes,
        "path_length": 0
    }

