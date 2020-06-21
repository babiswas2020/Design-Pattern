class Node:
   def __init__(self,value):
      self.value=value
      self.left=None
      self.right=None

   def mirror(self):
      temp1=None
      temp2=None
      if self:
        if self.left:
           temp1=self.left
        if self.right:
           temp2=self.right
        self.left=temp2
        self.right=temp1
        if self.left:
           self.left.mirror()
        if self.right:
           self.right.mirror()

   def inorder(self):
      if self:
        if self.left:
           self.left.inorder()
        print(self.value)
        if self.right:
           self.right.inorder()

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
   node.insert(18)
   node.insert(15)
   node.insert(24)
   node.insert(26)
   node.insert(6)
   node.insert(4)
   node.insert(10)
   node.insert(9)
   print("Inorder traversal of the tree")
   node.inorder()
   print("The mirror of the tree is:")
   node.mirror()
   print("The inorder of modified tree")
   node.inorder()

