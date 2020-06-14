from abc import ABC,abstractmethod

class Chair(ABC):
   @abstractmethod
   def get_chair(self):
       pass


class Medium_Chair(Chair):

    def __init__(self):
        self.length=30
        self.breadth=30
        self.height=30

    def get_chair(self):
        return self.__dict__

    def __str__(self):
        return "Medium Chair"


class Big_Chair(Chair):

    def __init__(self):
       self.length=40
       self.breadth=40
       self.height=40

    def get_chair(self):
       return self.__dict__

    def __str__(self):
       return "Big_Chair"

class Small_Chair:
   
    def __init__(self):
        self.length=50
        self.breadth=50
        self.height=50

    def get_chair(self):
        return self.__dict__

    def __str__(self):
       return "Small_Chair"

class ChairFactory:
    @staticmethod
    def get_chair_size(size):
        if size=="big":
           return Big_Chair()
        elif size=="small":
           return Small_Chair()
        elif size=="medium":
           return Medium_Chair()
        else:
           raise AssertionError("Invalid chair size")

if __name__=="__main__":
   size=input("Enter the size")
   obj=ChairFactory.get_chair_size(size)
   print(obj)
   print(obj.get_chair())






        
       