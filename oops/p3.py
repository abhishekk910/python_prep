class Vehicle():
    
    def __init__(self, make, model):
        self.make = make 
        self. model = model 

    def start_engine(self):
        # This method is meant to be overridden by child classes
        raise NotImplementedError("Subclass must implement abstract method")
    
 

class Car(Vehicle):

    def start_engine(self):
        return "The car's engine has started with a VROOM!"
    

class Motorcycle(Vehicle):

    def start_engine(self):
        return "The car's engine has started with a BRUM BRUM!"
    
def vehicle_start_up(vehicle):
    print(vehicle.start_engine())


car1 = Car("MS", "Swift")
bike = Motorcycle("TVS", "NTorq")

vehicle_start_up(car1)
vehicle_start_up(bike)

