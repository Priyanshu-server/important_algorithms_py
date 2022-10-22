class Graph(object):
    def __init__(self,V):
        self.V = V
        self.graph = [[0 for _ in range(self.V)]
                         for _ in range(self.V)]

    
    def printSolution(self,dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node,"\t\t",dist[node])


    def minDist(self,dist,visited):
        min = float('inf')

        for v in range(self.V):
            if dist[v] < min and visited[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    def dijkstra(self,src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        visited = [False] * self.V

        for _ in range(self.V):
            u = self.minDist(dist,visited)
            visited[u] = True

            for v in range(self.V):
                if(self.graph[u][v] > 0 and visited[v] == False and \
                    dist[v]> dist[u] + self.graph[u][v]): # prev. distance is more than the current one

                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)


g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]
g.dijkstra(0)