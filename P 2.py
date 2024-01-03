class Car:
    def __init__(self, car_id, brand, model, year, available=True):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.year = year
        self.available = available

    def __str__(self):
        availability = "Available" if self.available else "Not Available"
        return f"Car ID: {self.car_id}, Brand: {self.brand}, Model: {self.model}, Year: {self.year}, {availability}"


class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

    def __str__(self):
        return f"Customer ID: {self.customer_id}, Name: {self.name}"


class Rental:
    def __init__(self):
        self.rented_cars = []

    def rent_car(self, car, customer):
        if car.available:
            car.available = False
            self.rented_cars.append((car, customer))
            print(f"{customer.name} rented {car.brand} {car.model}.")
        else:
            print(f"Sorry, {car.brand} {car.model} is not available for rent.")

    def return_car(self, car, customer):
        if (car, customer) in self.rented_cars:
            car.available = True
            self.rented_cars.remove((car, customer))
            print(f"{customer.name} returned {car.brand} {car.model}.")
        else:
            print(f"This car is not rented by {customer.name}.")

    def display_rented_cars(self):
        if not self.rented_cars:
            print("No cars are currently rented.")
        else:
            print("Rented Cars:")
            for car, customer in self.rented_cars:
                print(f"{customer.name} - {car.brand} {car.model}")

car1 = Car(1, "Toyota", "Camry", 2022)
car2 = Car(2, "Honda", "Accord", 2021)
car3 = Car(3, "Ford", "Mustang", 2023)

customer1 = Customer(101, "John Doe")

rental_system = Rental()

rental_system.rent_car(car1, customer1)

rental_system.display_rented_cars()

rental_system.return_car(car1, customer1)

rental_system.display_rented_cars()
