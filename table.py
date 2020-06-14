from abc import ABC,abstractmethod

class Table(ABC):
    @abstractmethod
    def get_dimension(self):
        pass


class Big_Table(Table):

    def __init__(self):
        self.length=60
        self.breadth=60
        self.height=60

    def get_dimension(self):
        return self.__dict__

    def __str__(self):
        return "Big_Table"


class Small_Table(Table):

     def __init__(self):
         self.length=40
         self.breadth=40
         self.height=40

     def get_dimension(self):
         return self.__dict__

     def __str__(self):
        return "Small_Table"

class Medium_Table(Table):

     def __init__(self):
         self.length=50
         self.breadth=50
         self.height=50

     def get_dimension(self):
         return self.__dict__

     def __str__(self):
        return "Medium Table"


class Table_Factory:

     def get_table(size):
         if size=="big":
            return Big_Table()
         elif size=="small":
            return Small_Table()
         elif size=="medium":
            return Medium_Table()
         else:
            raise AssertionError("Invalid size")


         


