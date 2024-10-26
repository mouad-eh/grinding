from bfs import bfs_iterative
from dfs import dfs_iterative, dfs_recursive

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

#     1 -- 2
#    / |    |
#   3-- 4 --5

# Construct nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

# Establish edges (neighbors)
node1.neighbors = [node2, node3, node4]
node2.neighbors = [node1, node5]
node3.neighbors = [node1, node4]
node4.neighbors = [node1, node3, node5]
node5.neighbors = [node2, node4]

print("BFS iterative:")
bfs_iterative(node1)
print("DFS iterative:")
dfs_iterative(node1)
print("DFS recursive:")
dfs_recursive(node1, set())