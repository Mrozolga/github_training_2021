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


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.type = "cat"

    def speak(self):
        super().speak()
        print("Meow!")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise Exception(f"Not enough arguments or {sys.argv[3]} different than 'dog' or 'cat'!")
    if sys.argv[3] not in ['cat', 'dog']:
        raise Exception(f"{sys.argv[3]} different than 'dog' or 'cat'!")
    if sys.argv[3] == 'cat':
        called_animal = Cat(sys.argv[1], sys.argv[2])
    elif sys.argv[3] == 'dog':
        called_animal = Dog(sys.argv[1], sys.argv[2])
    called_animal.speak()

