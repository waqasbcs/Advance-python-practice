class Bird:
    def fly(self):
        print("Flying")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flying")

class Ostrich(Bird):
    def fly(self):
        print("Ostrich can't fly")

def make_bird_fly(bird):
    bird.fly()

bird1 = Sparrow()
bird2 = Ostrich()

make_bird_fly(bird1)  # Output: Sparrow flying
make_bird_fly(bird2)  # Output: Ostrich can't fly


# Classes are blueprints for objects.
# Objects are instances of classes.
# Encapsulation binds data and methods into a single unit.wrapping data and methods together in a single class.
# Inheritance allows a class to inherit from another class.

# Polymorphism allows different classes to be treated as instances of the same class through method overriding.
# polymorphism is the ablity of an object to take on many forms.same fuction but different methods

# Abstraction hides complex details to show only the necessary parts.
# OOP in Python makes it easier to design and maintain complex software systems by promoting reusable, 
# modular, and organized code.


