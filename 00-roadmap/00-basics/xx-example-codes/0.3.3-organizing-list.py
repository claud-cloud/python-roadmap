# -*- coding: utf-8 -*-

# Sort
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)  # Output: ['audi', 'bmw', 'subaru', 'toyota']

# Sort reverse
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort(reverse=True)
print(cars)  # Output: 'toyota', 'subaru', 'bmw', 'audi']

# Sort temporaly
cars = ["bmw", "audi", "toyota", "subaru"]

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# Reverse order
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)  # Output: ['bmw', 'audi', 'toyota', 'subaru']

cars.reverse()

print(cars)  # Output: ['subaru', 'toyota', 'audi', 'bmw']

# Length of a list
cars = ["bmw", "audi", "toyota", "subaru"]
print(len(cars))
