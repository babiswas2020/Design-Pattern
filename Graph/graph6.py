from collections import defaultdict

class Graph:
  def __init__(self,vertex):
      self.vertex=vertex
      self.graph=defaultdict(list)

  def add_edges(self,u,v):
      self.graph[u].append(v)

  def top_sort(self):
      count=0
      visited=[False]*self.vertex
      inward=[0]*self.vertex
      for i in range(self.vertex):
         for j in self.graph[i]:
            inward[j]=inward[j]+1
      queue=[]
      for i in range(self.vertex):
         if inward[i]==0:
            queue.append(i)
      while queue:
         m=queue.pop(0)
         print(m)
         for i in self.graph[m]:
            inward[i]=inward[i]-1
            if inward[i]==0:
               queue.append(i)
         count=count+1
      if count==self.vertex:
         print("Top sort is possible")
      else:
         print("There is a cycle in the graph")

if __name__=="__main__":
   graph=Graph(6)
   graph.add_edges(5,0)
   graph.add_edges(4,0)
   graph.add_edges(5,2)
   graph.add_edges(2,3)
   graph.add_edges(3,1)
   graph.add_edges(4,1)
   graph.top_sort()
   print("2nd Graph")
   graph=Graph(4)
   graph.add_edges(0,2)
   graph.add_edges(2,0)
   graph.add_edges(2,3)
   graph.add_edges(3,3)
   graph.add_edges(0,1)
   graph.add_edges(1,2)
   graph.top_sort()


            

         