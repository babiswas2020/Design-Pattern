class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def postorder(self):
       stack=[]
       root=self
       while True:
           if root:
             stack.append(root)
             root=root.left
           else:
                if not stack:
                   break
                if stack[-1].right==None:
                   print([obj.value for obj in stack])
                   root=stack.pop()
                   while stack[-1].right==root:
                       print([obj.value for obj in stack])
                       root=stack.pop()
                       if not stack:
                          break
                if stack:
                   root=stack[-1].right
                else:
                   break
               
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
   node.insert(23)
   node.insert(18)
   node.insert(15)
   node.insert(6)
   node.insert(4)
   node.insert(10)
   node.insert(9)
   print("Print all the path from root to node")
   node.postorder()

