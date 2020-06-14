class A:
  map={}
  def __init__(self):
     self.__dict__=A.map

class C(A):
   def __init__(self,**kwargs):
       A.__init__(self)
       A.map.update(kwargs)
   def __str__(self):
      return str(self.__dict__)


if __name__=="__main__":
  a=C(test1="Hello",test2="Bello")
  print(a)
  b=C(test4="mello")
  print(b)

