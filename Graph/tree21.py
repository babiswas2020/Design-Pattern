class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def leaf_nodes(self):
       def is_leaf(node):
          if not node:
            return False
          if node.left==None and node.right==None:
             return True
          return False

       stack=[]
       temp=None
       stack.append(self)
       while stack:
          temp=stack.pop()
          while temp and (not is_leaf(temp)):
              if temp.left:
                 stack.append(temp.left)
              if temp.right:
                 stack.append(temp.right)
              temp=stack.pop()
          if temp:
            if is_leaf(temp):
               print(temp.value)

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
          print("duplication not allowed")

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
   print("The inorder traversal of the tree")
   node.inorder()
   print("Print the leaf nodes")
   node.leaf_nodes()

   
   