class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print("Woof!")
import dog

my_dog = Dog("Rex", "SuperDog")
my_dog.bark()
