class UnionFind:
    def __init__(self, N):
        self.parents = list(range(N))

    def union(self, x, y):
        self.parents[self.find(x)] = self.find(y)

    def find(self, x):
        if self.parents[x] != x:
            return self.find(self.parents[x])
        return x
