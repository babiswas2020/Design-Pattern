class Cell:
   def __init__(self,x,y,dist):
       self.x=x
       self.y=y
       self.dist=dist


def is_valid(x,y,N,M):
    if x<0 or x>=N:
       return False
    if y<0 or y>=N:
       return False
    if M[x][y]=='#':
       return False
    return True


def find_steps(src,M,N):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    cell=Cell(src[0],src[1],0)
    queue=[]
    queue.append(cell)
    visited=[[False for i in range(N)] for i in range(N)]
    visited[src[0]][src[1]]=True
    while queue:
        m=queue.pop(0)
        if M[m.x][m.y]=='E':
           return m.dist
        for i in range(4):
            X=m.x+dx[i]
            Y=m.y+dy[i]
            if is_valid(X,Y,N,M) and visited[X][Y]==False:
                queue.append(Cell(X,Y,m.dist+1))
                visited[X][Y]=True

if __name__=="__main__":
  N=4
  M=[[3,3,1,'#'],[3,'#',3,3],['E',3,'#',3],['#',3,3,3]]
  src=[0,2]
  print(find_steps(src,M,N))



    
   
    



