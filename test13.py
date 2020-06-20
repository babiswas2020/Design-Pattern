class Director:

   def __init__(self,builder):
      self.builder=builder

   def construct_car(self):
       self.builder.create_car()
       self.builder.add_wheel("Wheel Added")
       self.builder.add_steering("Steering_added")
       self.builder.add_color("Color Added")

   def get_car(self):
       return self.builder.car

class Car:

   def __init__(self):
       self.wheel=None
       self.steering=None
       self.color=None

   def __str__(self):
      return f"{self.wheel} and {self.steering} and {self.color}"


class Builder:
   def __init__(self):
      self.car=None
   def create_car(self):
       self.car=Car()

class WorkShop(Builder):
    def add_wheel(self,str1):
        self.car.wheel=str1
    def add_steering(self,str1):
        self.car.steering=str1
    def add_color(self,str1):
        self.car.color=str1

if __name__=="__main__":
   builder=WorkShop()
   director=Director(builder)
   director.construct_car()
   print(director.get_car())



        