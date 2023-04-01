class Graph:
    def __init__(self, graph):
        self.graph = graph
        self. ROW = len(graph)
    def BFS(self, s, t, parent):
        visited = [False] * (self.ROW) 
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)         
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u                   
        return True if visited[t] else False
    def Ford_Fulkerson(self, entrances, exits):
        parent = [-1] * (self.ROW)  
        max_flow = 0        
        for e in entrances: 
            for x in exits:            
                while self.BFS(e, x, parent):                    
                    path_flow = float("Inf")
                    s = x
                    while(s != e):
                        path_flow = min(path_flow, self.graph[parent[s]][s])
                        s = parent[s]
                    max_flow += path_flow 
                    v = x 
                    while(v != e):
                        u = parent[v]
                        self.graph[u][v] -= path_flow
                        self.graph[v][u] += path_flow
                        v = parent[v]
        return max_flow

def solution(entrances, exits, path):
    g = Graph(path)        
    maxFlow = g.Ford_Fulkerson(entrances, exits)
    return maxFlow
