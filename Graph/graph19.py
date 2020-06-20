def stepping_number(n,m,num):
    queue=[]
    queue.append(num)
    while queue:
       number=queue.pop(0)
       if number>=n and number<=m:
          print(number)
       if number<n or number>m:
          continue
       num=number%10
       if num==0:
          queue.append(number*10+(num+1))
       elif num==9:
          queue.append(number*10+(num-1))
       else:
          queue.append(number*10+(num+1))
          queue.append(number*10+(num-1))

def stepping_number_input(n,m):
    for i in range(n,m):
       stepping_number(n,m,i)

if __name__=="__main__":
   stepping_number_input(0,21)

   

           