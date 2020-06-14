class A:
  def __new__(cls,*args,**kwargs):
      print("New method executed")
      return object.__new__(cls)
  def __init__(self,a,b):
      print("Init method executed")
      self.a=a
      self.b=b
  def __str__(self):
     return f"{self.a} and {self.b}"

if __name__=="__main__":
   a=A(2,3)
   print(a)
