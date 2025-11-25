class Vehicle:
    def __init__(self, vehicle_type, speed, num_wheeler):
        self.vehicle_type = vehicle_type
        self.speed = speed
        self.num_wheeler = num_wheeler

    def display(self):
        print(f"Vehicle Type: {self.vehicle_type}")
        print(f"Speed: {self.speed} km/h")
        print(f"Number of Wheels: {self.num_wheeler}")

class Car(Vehicle):
    def __init__(self, speed, num_wheeler=4):
        super().__init__("Car", speed, num_wheeler)

class Truck(Vehicle):
    def __init__(self, speed, num_wheeler=6):
        super().__init__("Truck", speed, num_wheeler)

def compare_speed(vehicle1, vehicle2):
    if vehicle1.speed > vehicle2.speed:
        print(f"{vehicle1.vehicle_type} is faster than {vehicle2.vehicle_type}")
    elif vehicle1.speed < vehicle2.speed:
        print(f"{vehicle2.vehicle_type} is faster than {vehicle1.vehicle_type}")
    else:
        print(f"Both {vehicle1.vehicle_type} and {vehicle2.vehicle_type} have the same speed")

# Test
car1 = Car(120)
truck1 = Truck(80)

print("Car Details:")
car1.display()
print("Truck Details:")
truck1.display()
print("Speed Comparison:")
compare_speed(car1, truck1)
