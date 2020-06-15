import copy

class Prototype:
    def __init__(self):
       self.obj={}

    def register_object(self,key,obj):
        if key not in self.obj:
           self.obj[key]=obj

    def unregister_object(self,key,obj):
         if key in self.obj:
            del self.obj[key]

    def clone(self,key,**attr):
        if key in self.obj:
           item=copy.deepcopy(self.obj.get(key))
           item.__dict__.update(attr)
           return item

class Car:
    def __init__(self):
        self.name=None
        self.color=None
        self.model=None

    def __str__(self):
        return f"{self.name} and {self.color} and {self.model}"


class Bus:

    def __init__(self):
       self.name=None
       self.color=None
       self.model=None

    def __str__(self):
        return f"{self.name} and {self.color} and {self.model}"

if __name__=="__main__":
   car=Car()
   bus=Bus()
   prototype=Prototype()
   prototype.register_object("car",car)
   prototype.register_object("bus",bus)
   car=prototype.clone("car",name="Test1",color="Red",model="New")
   print(car)
   bus=prototype.clone("bus",name="ASTC",color="Green",model="AX")
   print(bus)


   

