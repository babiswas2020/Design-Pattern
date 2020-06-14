import copy

class Prototype:
   def __init__(self):
      self.objects={}

   def register_object(self,name,obj):
      self.objects[name]=obj

   def unregister_object(self,name):
      del self.objects[name]

   def clone(self,name,**attr):
       obj=copy.deepcopy(self.objects.get(name))
       obj.__dict__.update(attr)
       return obj


class Car:
   def __init__(self):
       self.name="Skylark"
       self.color="Red"
       self.options="Ex"

   def __str__(self):
       return f"{self.name} and {self.color} and {self.options}"

if __name__=="__main__":
   car=Car()
   prototype=Prototype()
   prototype.register_object("car",car)
   c1=prototype.clone("car")
   print(c1)


   


       