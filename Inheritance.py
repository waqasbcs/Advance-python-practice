class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Some generic sound")

class Cat(Animal):
    def __init__(self, name, species):
        super().__init__(species)
        self.name = name

    def make_sound(self):
        print("Meow")

my_cat = Cat("Whiskers", "Feline")
print(my_cat.species)  # Output: Feline
my_cat.make_sound()    # Output: Meow
