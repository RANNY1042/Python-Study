class Dog:
    """개를 표현하는 클래스"""
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitiing.")

    def roll_over(self):
        print(f"{self.name} rolled over")

my_dog = Dog('Willie',6)
your_dog = Dog('Lucy',3)

print(f"My dog's name is {my_dog.name}")
print(f"My dog's {my_dog.age} years old.")
my_dog.sit()

print(f"Your dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old")
my_dog.sit()


class Car:
    """자동차를 표현하는 클래스"""

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
my_new_car = Car('audi','a4',2024)
print(my_new_car.get_descriptive_name())