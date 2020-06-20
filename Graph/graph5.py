from collections import defaultdict

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)

   def add_edges(self,u,v):
      self.graph[u].append(v)

   def top_sort_util(self,visited,stack,u):
       visited[u]=True
       for i in self.graph[u]:
          if not visited[i]:
             self.top_sort_util(visited,stack,i)
       stack.append(u)

   def topological_sort(self):
       stack=[]
       visited=[False]*self.vertex
       for i in range(self.vertex):
          if not visited[i]:
             self.top_sort_util(visited,stack,i)
             visited[i]=True
       while stack:
          print(stack.pop())

if __name__=="__main__":
   graph=Graph(6)
   graph.add_edges(5,4)
   graph.add_edges(5,0)
   graph.add_edges(5,2)
   graph.add_edges(2,3)
   graph.add_edges(3,1)
   graph.add_edges(4,1)
   graph.topological_sort()

   