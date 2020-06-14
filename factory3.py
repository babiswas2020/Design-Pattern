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
    pets=dict(dog=Dog("doggy"),cat=Cat("Mew"))
    return pets[pet]

if __name__=="__main__":
   dog=get_pet("dog")
   print(dog.speak())
   cat=get_pet("cat")
   print(cat.speak())
