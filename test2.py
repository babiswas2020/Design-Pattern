class A:
  instance=None
  def __new__(cls,*args,**kwargs):
      if A.instance==None:
         A.instance=object.__new__(cls)
         return A.instance
      else:
         raise Exception
  def __init__(self,a,b):
      self.a=a
      self.b=b
  def __str__(self):
     return f"{self.a} and {self.b}"

if __name__=="__main__":
   a=A(2,3)
   print(a)
   b=A(3,4)
   print(b)

