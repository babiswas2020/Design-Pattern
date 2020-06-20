import copy
class Car:
   def __init__(self):
       self.color=None
       self.model=None

   def __str__(self):
      return f"{self.color} and {self.model}"

class Bus:
   def __init__(self):
      self.color=None
      self.model=None

   def __str__(self):
      return f"{self.color} and {self.model}"


class Prototype:

   def __init__(self):
      self.obj=dict()

   def register(self,name,obj):
       if name not in self.obj:
           self.obj[name]=obj

   def unregister(self,name,obj):
      if name in self.obj:
         del self.obj[name]

   def clone(self,name,**attr):
       if name in self.obj:
          obj=copy.deepcopy(self.obj[name])
          obj.__dict__.update(attr)
          return obj

if __name__=="__main__":
   prototype=Prototype()
   prototype.register("car",Car())
   prototype.register("bus",Bus())
   obj=prototype.clone("car",color="Green",model="new")
   print(obj)
   obj=prototype.clone("bus",color="Red",model="New")
   print(obj)

   
   


