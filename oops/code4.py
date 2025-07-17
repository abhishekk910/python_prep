class Car:
    # A class variable to keep track of the total number of cars produced.
    _total_cars_produced = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        # Every time a new Car instance is created, we increment the class variable.
        Car._total_cars_produced += 1
        print(f"A new car has been produced: {self.make} {self.model}")

    @classmethod
    def get_total_cars(cls):
        """
        This is a class method.
        It takes 'cls' (the class itself) as its first argument.
        It returns the total number of cars that have been created.
        """
        return cls._total_cars_produced

# --- Demonstration ---

# Produce some cars
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")
car3 = Car("Ford", "Mustang")
car4 = Car("Tesla", "Model 3")

# We can call the class method directly on the Car class
total_count_class_call = Car.get_total_cars()
print(f"\nTotal number of cars produced (called from class): {total_count_class_call}")

# We can also call it from any instance, and it will return the same value
total_count_instance_call = car3.get_total_cars()
print(f"Total number of cars produced (called from instance): {total_count_instance_call}")