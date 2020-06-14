from furnitureFactory import FurnitureFactory


if __name__=="__main__":
   chair=FurnitureFactory.get_furniture("chair","small")
   print(chair.get_dimension())
   table=FurnitureFactory.get_furniture("table","big")
   print(table.get_dimension())


   