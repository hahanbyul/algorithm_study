# https://algospot.com/judge/problem/read/GALLERY
import pprint as p


class Gallery:
    def __init__(self, G, H):
        self.observed = set()
        self.gallery = G
        self.hall = H

        self.graph = [[0 for _ in range(G)] for _ in range(G)]
    def read_graph(self):
        for _ in range(self.hall):
            self.read_edge(raw_input())

    def read_graph_as_string(self, str_graph):
        for str_edge in str_graph.split('\n'):
            self.read_edge(str_edge)

    def read_edge(self, str_edge):
        u, v = [int(i) for i in str_edge.split()]
        self.set_edge(u, v)

    def set_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def off_edge(self, u, v):
        self.graph[u][v] = 0
        self.graph[v][u] = 0

        self.hall -= 1

        self.observed.add(u)
        self.observed.add(v)

    def get_not_observed_galleries(self, u):
        return set([u] + [i for i, is_edge in enumerate(self.graph[u]) if is_edge]) - self.observed

    def solve(self):
        camera = 0
        while len(self.observed) != self.gallery and self.hall > 0:
            possible_galleries = [self.get_not_observed_galleries(u) for u in range(self.gallery)]
            # p.pprint(possible_galleries)
            num_galleries = [len(s) for s in possible_galleries]
            u = num_galleries.index(max(num_galleries))
            covered_galleries = possible_galleries[u]
            self.observed = self.observed | covered_galleries
            # print(self.observed)
            
            for v, is_edge in enumerate(self.graph[u]):
                if not is_edge:
                    continue
                self.off_edge(u, v)
            camera += 1
            # p.pprint(self.graph)
            # print(f'H: {self.hall}')
        camera += self.gallery - len(self.observed)
        # print(f'camera: {camera}')
        return camera


def main():
    C = int(raw_input())
    for _ in range(C):
        G, H = [int(i) for i in raw_input().split()]
        gallery = Gallery(G, H)
        gallery.read_graph()
        print gallery.solve()


if __name__ == '__main__':
    main()
