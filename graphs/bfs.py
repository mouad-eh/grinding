"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

def bfs_iterative(snode):
    if not snode:
        return
    q = deque([snode])
    visited = set()
    while q:
        node = q.popleft()
        if node in visited:
            continue
        print(node.val)
        visited.add(node)
        for neighbor in node.neighbors:
            if neighbor not in visited:
                q.append(neighbor)

# bfs recursive does not have any meaning.
# It just tries to make the iterative solution recursive