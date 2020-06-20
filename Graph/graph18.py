class Cell:
   def __init__(self,x,dist):
       self.x=x
       self.dist=dist

def is_valid(x,N):
    if x<0 or x>=N:
       return False
    return True

def find_steps(arr,N):
   dx=[1,-1]
   visited=[False]*N
   queue=[]
   queue.append(Cell(0,0))
   visited[0]=True
   while queue:
       m=queue.pop(0)
       if m.x==N-1:
          return m.dist
       for i in range(2):
          X=m.x+dx[i]
          if is_valid(X,N) and visited[X]==False:
             queue.append(Cell(X,m.dist+1))
             visited[X]=True
       l=[i for i,j in enumerate(arr) if j==arr[m.x]]
       for i in l:
          if not visited[i]:
             queue.append(Cell(i,m.dist+1))
             visited[i]==True

if __name__=="__main__":
   l=[0,1,2,3,4,5,6,7,5,4,3,6,0,1,2,3,4,5,7]
   N=len(l)
   print(find_steps(l,N))
   

