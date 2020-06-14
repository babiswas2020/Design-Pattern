class Dog:
   def __init__(self,name):
      self.name=name
   def speak(self):
       return "Woof"

class Cat:
   def __init__(self,name):
       self.name=name
   def speak(self):
       return "Mew"

def get_pet(pet="dog"):
    pets=dict(dog=Dog("dog1"),cat=Cat("pussy"))
    return pets[pet]

if __name__=="__main__":
   d=get_pet("dog")
   print(d.speak())
   c=get_pet("cat")
   print(c.speak())



    