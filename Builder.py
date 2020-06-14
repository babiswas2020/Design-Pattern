class Director:

   def __init__(self,builder):
       self.builder=builder

   def construct_car(self):
       self.builder.create_car()
       self.builder.add_wheel()
       self.builder.add_color()
       self.builder.add_model()

   def get_car(self):
      return self.builder.car
       
class Builder:
    def __init__(self):
        self.car=None
    def create_car(self):
        self.car=Car()

class Car_Maker(Builder):
   def add_wheel(self):
       self.car.wheel="Wheel added"
   def add_color(self):
       self.car.color="Color added"
   def add_model(self):
       self.car.model="Model Added"
       


class Car:

  def __init__(self):
     self.wheel=None
     self.color=None
     self.model=None

  def __str__(self):
     return f"{self.wheel} and {self.color} and {self.model}"

if __name__=="__main__":
   builder=Car_Maker()
   director=Director(builder)
   director.construct_car()
   car=director.get_car()
   print(car)

   

