"""


IT Clash - <g>learn

Checkpoint : ⭐⭐⭐

Find minimum spanning tree graph using Prim's Algorithm or Kruskal if u want

Using minheap instead heap for less time complexity


"""

class MinHeap:
    def __init__(self):
        """Initializing heap"""
        self.heap = []

    def push(self, item):
        """Push data to heap"""
        self.heap.append(item)
        self.sift_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        self.swap(0, len(self.heap) - 1)
        item = self.heap.pop()
        self.sift_down(0)
        return item

    def sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i][0] < self.heap[parent][0]:
                self.swap(i, parent)
                i = parent
            else:
                break

    def sift_down(self, i):
        size = len(self.heap)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < size and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            if right < size and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right
            if smallest != i:
                self.swap(i, smallest)
                i = smallest
            else:
                break

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def is_empty(self):
        return len(self.heap) == 0

class CheckpointsGraph:
    def __init__(self, n):
        self.size = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, weight: int, u: int, v: int):
        self.adj[u].append((weight, v))
        self.adj[v].append((weight, u))

    def prim(self, start: int) -> int:
        visited = [False] * self.size
        heap = MinHeap()
        heap.push((0, start))
        total_cost = 0
        count = 0

        while not heap.is_empty() and count < self.size:
            weight, u = heap.pop()
            if visited[u]:
                continue
            visited[u] = True
            total_cost += weight
            count += 1

            for w, v in self.adj[u]:
                if not visited[v]:
                    heap.push((w, v))

        return total_cost if count == self.size else -1

def main():
    N, M = map(int, input().split())
    graph = CheckpointsGraph(N)

    for _ in range(M):
        u, v, weight = map(int, input().split())
        graph.add_edge(weight, u - 1, v - 1)

    start = int(input()) - 1
    print(graph.prim(start))

main()
