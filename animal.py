import sys


class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("I am", self.name, "and I am", self.age, "years old")


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.type = "dog"

    def speak(self):
        super().speak()
        print("Woof!")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Not enough arguments!")
    called_animal = Dog(sys.argv[1], sys.argv[2])
    called_animal.speak()

