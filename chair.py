from abc import ABC,abstractmethod

class Chair(ABC):
    """ Abstarct class for chair """

    @abstractmethod
    def get_dimension(self):
        pass

class Medium_Chair(Chair):
      """ Medium chair class """

      def __init__(self):
           self.length=30
           self.breadth=30
           self.height=30

      def get_dimension(self):
          return self.__dict__
      
      def __str__(self):
          return "Medium Chair"


class Big_Chair(Chair):
    """ Big chair class """

    def __init__(self):
        self.length=40
        self.breadth=40
        self.height=40

    def get_dimension(self):
        return self.__dict__

    def __str__(self):
       return "Big Chair"

class Small_Chair(Chair):
     """Small chair class"""

     def __init__(self):
         self.length=50
         self.breadth=50
         self.height=50

     def get_dimension(self):
         return self.__dict__

     def __str__(self):
        return "Small Chair"



class Chair_Factory:
    """Chair factory class"""

    @staticmethod
    def get_chair(size):
        if size=="big":
           return Big_Chair()
        elif size=="small":
           return Small_Chair()
        elif size=="medium":
           return Medium_Chair()
        else:
           raise AssertionError("Wrong key type")



        
