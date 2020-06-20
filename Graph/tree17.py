class Node:
  def __init__(self,value):
      self.value=value
      self.left=None
      self.right=None

  def right_view(self):
     str1=""
     queue=[]
     queue.append(self)
     while queue:
         q_len=len(queue)
         str1+=str(queue[-1].value)+" "
         while q_len:
            m=queue.pop(0)
            if m.left:
               queue.append(m.left)
            if m.right:
               queue.append(m.right)
            q_len=q_len-1
     return str1

  def insert(self,value):
      if self.value>value:
         if self.left:
            self.left.insert(value)
         else:
            self.left=Node(value)
      elif self.value<value:
         if self.right:
            self.right.insert(value)
         else:
            self.right=Node(value)
      else:
         print("Duplication not allowed")

if __name__=="__main__":
   node=Node(12)
   node.insert(22)
   node.insert(24)
   node.insert(26)
   node.insert(18)
   node.insert(15)
   node.insert(6)
   node.insert(4)
   node.insert(10)
   node.insert(9)
   print("The right view of the Tree")
   print(node.right_view())

