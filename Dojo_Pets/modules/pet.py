# Create a Pet class with attributes
# Implement methods for Pet class
class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.noise = noise
        self.health = 100
        self.energy = 50

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        self.energy -= 15
        return self

    def noise(self):
        print(self.noise)

# User inheritance to create sub classes of pets
class Dog(Pet):
    def __init__(self, noise):
        self.noise = noise

    def noise(self):
        print("woof")

class Cat(Pet):
    def __init__(self, noise):
        self.noise = noise

    def noise(self):
        print("meow")