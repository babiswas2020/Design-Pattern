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

   def lca(self,val1,val2):
      if self:
         if self.is_present(val1) and self.is_present(val2):
           if self.value==val1 or self.value==val2:
              return self
           else:
             if self.left:
                temp1=self.left.lca(val1,val2)
             if self.right:
                temp2=self.right.lca(val1,val2)
             if temp1:
                return temp1
             elif temp2:
                return temp2
             else:
                return self
         else:
            return None
      else:
         return None
        

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

   def is_present(self,val):
       if self:
          if self.value==val:
             return True
          else:
             return self.left.is_present(val) or self.right.is_present(val)

if __name__=="__main__":
   node=Node(12)
   node.insert(22)
   node.insert(24)
   node.insert(18)
   node.insert(15)
   node.insert(20)
   node.insert(26)
   node.insert(23)
   node.insert(6)
   node.insert(4)
   node.insert(10)
   node.insert(8)
   print("Inorder traversal of the tree")
   node.inorder()
   print("The lca of the 20 and 24")
   test=node.lca(20,24)
   print(test.value)

        
       
