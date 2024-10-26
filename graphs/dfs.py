"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
def dfs_iterative(snode):
    if not snode:
        return []

    visited = set()
    stack = [snode]

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        print(node.val)

        # Add neighbors in reverse order to maintain left-to-right traversal
        for neighbor in reversed(node.neighbors):
            if neighbor not in visited:
                stack.append(neighbor)

def dfs_recursive(node, visited):
    if node in visited:
        return

    visited.add(node)
    print(node.val)

    for neighbor in node.neighbors:
        dfs_recursive(neighbor, visited)