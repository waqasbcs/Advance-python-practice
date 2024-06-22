class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking")

my_dog = Dog("Rex", 5)
print(my_dog.name)  # Output: Rex
my_dog.bark()       # Output: Rex is barking
