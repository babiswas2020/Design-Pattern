from table import Table_Factory
from chair import Chair_Factory
from abc import ABC,abstractmethod

class Furniture(ABC):
     @abstractmethod
     def get_furniture(furniture,size):
         pass

class FurnitureFactory(Furniture):
     
     
     @staticmethod
     def get_furniture(furniture,size):
         try:
            if furniture=="chair":
                 return Chair_Factory.get_chair(size)
            elif furniture=="table":
                 return Table_Factory.get_table(size)
            else:
                 raise AssertionError("Invalid furniture type")
         except Exception as e:
            print(e)
          
            
            
            
