"""

IT Clash - <g>learn

Network Engineer : ⭐⭐⭐

Find cut edge from graph


"""



class cityGraph:
    def __init__(self, cities: list[str]):
        self.size = len(cities)
        self.adj = [[0] for _ in range(self.size)]

    def add_edge(self, city: str, target: str):
        self.adj[self.adj.index(target)] = city
        self.adj[self.adj.index(city)] = target

    