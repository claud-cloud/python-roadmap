# -*- coding: utf-8 -*-

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# Writing Clear Prompts

name = input("Please enter your name: ")
print(f"\nHello, {name}!")

# long prompt
prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)

print(f"\nHello, {name}!")

# int

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
