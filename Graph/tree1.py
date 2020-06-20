class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def postorder(self):
       if self:
          if self.left:
             self.left.postorder()
          if self.right:
             self.right.postorder()
          print(self.value)

   def preorder(self):
       if self:
          print(self.value)
          if self.left:
             self.left.preorder()
          if self.right:
             self.right.preorder()

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
   print("Creating Tree")
   node=Node(12)
   node.insert(22)
   node.insert(26)
   node.insert(24)
   node.insert(28)
   node.insert(6)
   node.insert(4)
   node.insert(10)
   node.insert(9)
   print("Inorder traversal of the tree")
   node.inorder()
   print("Preorder traversal of the tree")
   node.preorder()
   print("Postorder traversal of the tree")
   node.postorder()
