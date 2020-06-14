from chair import Chair_Factory

if __name__=="__main__":
   chair=Chair_Factory.get_chair("medium")
   print(chair.get_dimension())
   chair=Chair_Factory.get_chair("small")
   print(chair.get_dimension())
   chair=Chair_Factory.get_chair("big")
   print(chair.get_dimension())


