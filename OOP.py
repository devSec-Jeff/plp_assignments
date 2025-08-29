class Car:
    def __init__(self, brand, year):
        brand = brand
        year = year

    def move(self):
        print("Driving")

    def makeSound(self):
        print(f'Car goes vroom! vroom!')

class Dog:
    def __init__(self, name, breed):
        name = name
        breed = breed

    def move(self):
        print("Running")

    def makeSound(self):
        print(f'Dog is barking woof! woof!')


car1 = Car('Mercedez', 2015)
dog1 = Dog('Carlos', 'German Shephered')


car1.move()
car1.makeSound()

dog1.move()
dog1.makeSound()
