# -*- coding: utf-8 -*-

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)  # Output: ['honda', 'yamaha', 'suzuki']

# Modifying elements
motorcycles[0] = "ducati"
print(motorcycles)  # Output: ['ducati', 'yamaha', 'suzuki']

# Adding elements

## to the end
motorcycles.append("ducati")
print(motorcycles)  # Output: ['ducati', 'yamaha', 'suzuki', 'ducati']

## new elements
motorcycles = []

motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")

print(motorcycles)  # Output: ['ducati', 'yamaha', 'suzuki']

# Inserting elements
motorcycles = ["honda", "yamaha", "suzuki"]

motorcycles.insert(0, "ducati")

print(motorcycles)  # Output: ['ducati', 'honda', 'yamaha', 'suzuki']

# Removing elements

# del statement
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)  # Output: ['honda', 'yamaha', 'suzuki']

del motorcycles[0]
print(motorcycles)  # Output: ['yamaha', 'suzuki']

# pop() method
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)  # Output: ['honda', 'yamaha', 'suzuki']

# Elimina el ultimo elemento y lo devuelve almacenandolo en popped_motorcycle
popped_motorcycle = motorcycles.pop()

print(motorcycles)  # Output: ['honda', 'yamaha']

print(popped_motorcycle)  # Output: suzuki

## Last element
motorcycles = ["honda", "yamaha", "suzuki"]
last_owned = motorcycles.pop(0)
print(
    f"The first motorcycle I owned was a {last_owned.title()}."
)  # Output: The first motorcycle I owned was a Honda.


## first element
motorcycles = ["honda", "yamaha", "suzuki"]
first_owned = motorcycles.pop(0)
print(
    f"The first motorcycle I owned was a {first_owned.title()}."
)  # Output: The first motorcycle I owned was a Honda.

# Removing elements
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)  # Output: ['honda', 'yamaha', 'suzuki', 'ducati']

motorcycles.remove("ducati")
print(motorcycles)  # Output: ['honda', 'yamaha', 'suzuki']

# remove and use element
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)  # Output: ['honda', 'yamaha', 'suzuki', 'ducati']

too_expensive = "ducati"
motorcycles.remove(too_expensive)

print(motorcycles)  # Output: ['honda', 'yamaha', 'suzuki']
print(
    f"\nA {too_expensive.title()} is too expensive for me."
)  # Output: A Ducati is too expensive for me.
