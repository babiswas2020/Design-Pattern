class Cell:
   def __init__(self,x,y,dist):
       self.x=x
       self.y=y
       self.dist=dist


def is_valid(x,y,N):
   if x<0 or x>=N:
      return False
   if y<0 or y>=N:
      return False
   return True


def find_steps(src,dest,N):
   dx=[2,2,-2,-2,1,-1,1,-1]
   dy=[1,-1,1,-1,2,2,-2,-2]
   queue=[]
   visited=[[0 for i in range(N)] for i in range(N)]
   cell=Cell(src[0],src[1],0)
   queue.append(cell)
   visited[src[0]][src[1]]=1
   while queue:
       m=queue.pop(0)
       if m.x==dest[0] and m.y==dest[1]:
          return m.dist
       for i in range(8):
          x=m.x+dx[i]
          y=m.y+dy[i]
          if is_valid(x,y,N) and visited[x][y]==False:
             queue.append(Cell(x,y,m.dist+1))
             visited[x][y]=True

if __name__=="__main__":
   src=(2,2)
   dest=(4,5)
   N=6
   print(find_steps(src,dest,6))

   
   
   