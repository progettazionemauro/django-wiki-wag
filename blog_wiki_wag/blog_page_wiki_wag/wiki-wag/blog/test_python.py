class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle started.")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} car started.")

class CarWithSuper(Car):
    def __init__(self, brand, model, color):
        super().__init__(brand, model)
        self.color = color

    def start(self):
        super().start()
        print(f"The {self.color} car is ready to go.")

    def __getattribute__(self, name):
        # Avoid recursion by using super().__getattribute__
        if name == "brand":
            return "Awesome " + super().__getattribute__('brand')
        else:
            return super().__getattribute__(name)

# Creating an instance of CarWithSuper
car_with_super = CarWithSuper(brand="FIAT", model="Mustang", color="red")
print(car_with_super.brand)  # Output: Awesome Ford
car_with_super.start()  # Output: Ford Mustang car started. The red car is ready to go.

car_without_super = Car(brand="Toyota", model="Camry")
print(car_without_super.model)  # Output: Camry

