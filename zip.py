person = Person("Alice", 30)
print(person.get_age())  # Output: 30


names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 95]

# Using zip to combine lists
for name, score in zip(names, scores):
    print(f'{name} scored {score}')