# -*- coding: utf-8 -*-

bicycles = ["trek", "cannondale", "redline", "specialized"]

# con print() Python imprime una representación de la lista
print(bicycles)  # ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])  # trek
print(bicycles[0].title())  # Output: Trek

print(bicycles[1])  # Output: cannondale
print(bicycles[3])  # Output: specialized

# Ultimos elementos
print(bicycles[-1])  # Output: specialized
print(bicycles[-2])  # Output: redline
print(bicycles[-3])  # Output: cannondale


# Using Individual Values from a List
message = f"My first bicycle was a {bicycles[0].title()}."

print(message)

# Exercise 1 - names
names = ["Jose luis", "Ramon", "Raul", "Copito", "Luna", "Flor"]

print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])

# Exercise 2 - greetings
print(f"Hola {names[0]}!, Mucho gusto")
print(f"Hola {names[1]}!, Mucho gusto")
print(f"Hola {names[2]}!, Mucho gusto")
print(f"Hola {names[3]}!, Mucho gusto")
print(f"Hola {names[4]}!, Mucho gusto")
print(f"Hola {names[5]}!, Mucho gusto")

# Excercise 3 - vehicles
vehicles = ["motorcycle", "automobile", "airplane", "boat"]

print(f"I would like to own a {vehicles[2]}!")
