class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def preorder(self):
       stack=[]
       stack.append(self)
       while stack:
          m=stack.pop()
          print(m.value)
          if m.right:
            stack.append(m.right)
          if m.left:
            stack.append(m.left)
           
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
   node.insert(24)
   node.insert(18)
   node.insert(26)
   node.insert(15)
   node.insert(6)
   node.insert(4)
   node.insert(10)
   node.insert(5)
   node.preorder()

