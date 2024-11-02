import periodictable

Atomic_No = int(input("Enter Atomic No: "))
element = periodictable.elements[Atomic_No]

print('Name:', element.name)
print('Symbol:', element.symbol)
print('Atomic mass:', element.mass)
print('Density:', element.density)


# Enter Atomic No: 12
# Name: magnesium
# Symbol: Mg     
# Atomic mass: 24.305
# Density: 1.738