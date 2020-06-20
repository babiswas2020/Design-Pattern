from collections import defaultdict

class Graph:
    def __init__(self,vertex):
        self.vertex=vertex
        self.graph=defaultdict(list)

    def add_edges(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def find_shortest_path_util(self,u,v):
        prev=self.find_shortest_path(u)
        path=[]
        i=v
        while i!=None:
          path.append(i)
          i=prev[i]
        path[:]=path[::-1]
        if path[0]==u:
           print(f"The shortcut path is {path}")
        else:
           print(f"There is no path from {u} and {v}") 
                   

    def find_shortest_path(self,u):
        queue=[]
        visited=[False]*self.vertex
        prev=[None]*self.vertex
        queue.append(u)
        visited[u]=True
        while queue:
           m=queue.pop(0)
           for i in self.graph[m]:
              if not visited[i]:
                 queue.append(i)
                 visited[i]=True
                 prev[i]=m
        return prev

if __name__=="__main__":
   graph=Graph(8)
   graph.add_edges(1,2)
   graph.add_edges(1,0)
   graph.add_edges(0,3)
   graph.add_edges(3,7)
   graph.add_edges(3,4)
   graph.add_edges(7,4)
   graph.add_edges(7,6)
   graph.add_edges(4,6)
   graph.add_edges(4,5)
   graph.add_edges(6,5)
   graph.find_shortest_path_util(0,7)
   
   

        
