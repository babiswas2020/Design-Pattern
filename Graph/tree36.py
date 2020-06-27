class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def search(self,value):
       temp1=None
       temp1=self
       while temp1:
           if temp1.value>value:
              temp1=temp1.left
           elif temp1.value<value:
              temp1=temp1.right
           else:
              return temp1
       return temp1

   def minm(self):
       root=self
       if root:
          while root.left:
              root=root.left
          return root
       else:
          return None
             
   def inorder_sucessor(self,node):
       temp2=None
       temp1=None
       if node.right:
          return node.right.minm()
       else:
        temp1=self
        while temp1:
          if node.value>temp1.value:
             temp1=temp1.right
          elif node.value<temp1.value:
             temp2=temp1
             temp1=temp1.left
          else:
             return temp2
             
       
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
          
   def inorder(self):
       if self:
          if self.left:
             self.left.inorder()
          print(self.value)
          if self.right:
             self.right.inorder()

if __name__=="__main__":
   node=Node(12)
   node.insert(22)
   node.insert(24)
   node.insert(18)
   node.insert(15)
   node.insert(26)
   node.insert(23)
   node.insert(6)
   node.insert(4)
   node.insert(10)
   node.insert(9)
   print("Inorder traversal of the tree")
   node.inorder()
   test=node.search(18)
   print(test.value)
   print("The inorder sucessor of the tree")
   print(node.inorder_sucessor(test).value)
   


