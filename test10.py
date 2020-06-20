class A:
  def __init__(self,a,b):
      self.a=a
      self.b=b

  def __str__(self):
      return f"{self.a} and {self.b}"

  @property
  def seta(self):
     return self.a

  @property
  def setb(self):
     return self.b

  @seta.setter
  def seta(self,a):
      self.a=a

  @setb.setter
  def setb(self,b):
      self.b=b

if __name__=="__main__":
   a=A(2,3)
   print(a)
   print(a.__dict__)
   print(a.seta)
   print(a.setb)
   a.seta=12
   a.setb=13
   print(a.__dict__)

   
   