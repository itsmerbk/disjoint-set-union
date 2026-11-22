class DSU:
    def __init__(self, n):
        self.p, self.r, self.count = list(range(n)), [0]*n, n
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]; x = self.p[x]
        return x
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb: return False
        if self.r[ra] < self.r[rb]: ra, rb = rb, ra
        self.p[rb] = ra
        if self.r[ra] == self.r[rb]: self.r[ra] += 1
        self.count -= 1; return True

if __name__ == "__main__":
    d = DSU(5); d.union(0, 1); d.union(1, 2); d.union(3, 4)
    assert d.find(0) == d.find(2) and d.count == 2
    print("[PASS] 004_disjoint_set_union")
