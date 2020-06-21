class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def inorder(self):
       if self:
          if self.left:
             self.left.inorder()
          print(self.value)
          if self.right:
             self.right.inorder()

   def zig_zag(self):
      stack1=[]
      stack2=[]
      stack1.append(self)
      while stack1 or stack2:
          while stack1:
             m=stack1.pop()
             print(m.value)
             if m.left:
                stack2.append(m.left)
             if m.right:
                stack2.append(m.right)
          while stack2:
             n=stack2.pop()
             print(n.value)
             if n.right:
                stack1.append(n.right)
             if n.left:
                stack1.append(n.left)
          
       
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
   print("The inorder traversal of the tree is:")
   node.inorder()
   print("The zigzag traversal of the tree is:")
   node.zig_zag()
