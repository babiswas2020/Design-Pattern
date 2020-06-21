class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def common_nodes(self,node):
       stack1=[]
       stack2=[]
       root=self
       while True:
           if root:
              stack1.append(root)
              root=root.left
           elif node:
              stack2.append(node)
              node=node.left
           elif stack1 and stack2:
              root=stack1[-1]
              node=stack2[-1]
              if root.value==node.value:
                 print(root.value)
                 stack1.pop()
                 stack2.pop()
                 node=node.right
                 root=root.right
              elif root.value>node.value:
                   root=None
                   stack2.pop()
                   node=node.right
              elif root.value<node.value:
                   node=None
                   stack1.pop()
                   root=root.right
           else:
              break
          
                 

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
   print("Constructing the first tree")
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
   print("Constructing the 2nd tree")
   node1=Node(14)
   node1.insert(21)
   node1.insert(23)
   node1.insert(18)
   node1.insert(15)
   node1.insert(6)
   node1.insert(5)
   node1.insert(10)
   node1.insert(12)
   print("Common nodes of the tree")
   node.common_nodes(node1)
   
   
   