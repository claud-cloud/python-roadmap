# -*- coding: utf-8 -*-

num_str = "12"
num_int = 23

print(
    "Data type of num_str before Type Casting:", type(num_str)
)  # Output: Data type of num_str before Type Casting: <class 'str'>

# explicit type conversion
num_str = int(num_str)

print(
    "Data type of num_str after Type Casting:", type(num_str)
)  # Output: Data type of num_str after Type Casting: <class 'int'>

num_sum = num_int + num_str

print("Sum:", num_sum)  # Output: Sum: 35
print(
    "Data type of num_sum:", type(num_sum)
)  # Output: Data type of num_sum: <class 'int'>
