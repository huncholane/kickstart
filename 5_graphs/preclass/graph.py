class Graph:
    def __init__(self, size):
        self.adj_list = [[] for _ in range(size)]
        self.v = size
        self.num_odd = 0

    def add_edge(self, start, end, bidir=True):
        self.adj_list[start].append(end)
        if len(self.adj_list[start]) % 2 == 1:
            self.num_odd += 1
        else:
            self.num_odd -= 1
        if bidir:
            self.adj_list[end].append(start)
            if len(self.adj_list[end]) % 2 == 1:
                self.num_odd += 1
            else:
                self.num_odd -= 1

    def has_eulerian_cycle(self):
        return self.num_odd == 0

    def has_eulerian_path(self):
        return self.num_odd == 0 or self.num_odd == 2

    # def search(self, s):
    #     captured[s]=1
    #     while fringe:
    #         pick one from fringe => (u,v)
    #         captured[v]=1
    #         parent[v]=u

    def stack_dfs(self, s):
        # LIFO queue (stack)
        visited = [False] * self.v
        parent = [None] * self.v
        q = [s]
        visited[s] = True
        while q:
            v = q.pop()
            for w in self.adj_list[v]:
                if not visited[w]:
                    visited[w] = True
                    parent[w] = v
                    q.append(w)

    def rec_dfs(self, s):
        # Keeps same order where lifo makes it backwards
        visited = [False] * self.v
        parent = [None] * self.v

        def dfs(s):
            visited[s] = True
            for w in self.adj_list[s]:
                if not visited[w]:
                    parent[w] = s
                    dfs(w)

        dfs(s)

    def bfs(self, s):
        # FIFO queue
        captured = [0] * self.v
        visited = [0] * self.v
        parent = [None] * self.v
        captured[s] = 1
        visited[s] = 1
        q = [s]
        while q:
            v = q.pop(0)
            captured[v] = 1
            for w in self.adj_list[v]:
                if not visited[w]:
                    visited[w] = 1
                    parent[w] = v
                    q.append(w)
                else:
                    print(f"Found cycle from {v} to {w}")
        print(f"{s} has {sum(captured)} vertices in it's connected components")

    def __str__(self):
        s = f"{self.v} vertex graph, {self.num_odd} with odd degree\n"
        s += f'{"✅" if self.has_eulerian_cycle() else "❌"} Eulerian Cycle\n'
        s += f'{"✅" if self.has_eulerian_path() else "❌"} Eulerian Path\n'
        for i, l in enumerate(self.adj_list[:]):
            s += f"{i} -> {l}"
            if i != self.v - 1:
                s += "\n"
        return s


g = Graph(10)
g.add_edge(0, 1)
# g.add_edge(0, 6)
# g.add_edge(0, 8)
g.add_edge(0, 4)
g.add_edge(1, 4)
print(g)
g.bfs(1)
