class Director:

   def __init__(self,builder):
       self.builder=builder

   def construct_car(self):
       self.builder.create_car()
       self.builder.add_wheels()
       self.builder.add_color()
       self.builder.add_model()

   def get_car(self):
       return self.builder.car


class Builder:

     def __init__(self):
         self.car=None

     def create_car(self):
         self.car=Car()

class Workshop(Builder):
     def add_wheels(self):
         self.car.wheels="Wheels Added"
     def add_color(self):
         self.car.color="Color Added"
     def add_model(self):
         self.car.model="Model Added"

class Car:

   def __init__(self):
       self.wheels=None
       self.color=None
       self.model=None

   def __str__(self):
       return f"{self.wheels} and {self.color} and {self.model}"

if __name__=="__main__":
   builder=Workshop()
   director=Director(builder)
   director.construct_car()
   car=director.get_car()
   print(car)

   

   
   
