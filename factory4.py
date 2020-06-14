class Dog:
   def speak(self):
      return "Woof"
   def __str__(self):
       return "Doggy"


class Dog_Factory:
    def get_pet(self):
        return Dog()
    def get_food(self):
        return "Meat"


class Pet_Factory:
     def __init__(self,pet_factory):
         self.pet_factory=pet_factory

     def show_pet(self):
         pet=self.pet_factory.get_pet()
         pet_food=self.pet_factory.get_food()
         print(f"Our pet is {pet}")
         print(f"Our pet says {pet.speak()}")
         print(f"Our pet eat {pet_food}")

if __name__=="__main__":
   factory=Dog_Factory()
   pet_factory=Pet_Factory(factory)
   pet_factory.show_pet()


         