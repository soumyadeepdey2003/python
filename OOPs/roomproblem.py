class Room:
    def __init__(self,height,width,breadth):
        self.h=height
        self.w=width
        self.b=breadth

    def vol(self):
        return(self.h * self.b * self.w)
    
room1 = Room(10, 20, 30)
room2 = Room(5, 6, 7)
room3 = Room(4, 8, 3)


print("Volume of Room 1:", room1.vol())
print("Volume of Room 2:", room2.vol())
print("Volume of Room 3:", room3.vol())