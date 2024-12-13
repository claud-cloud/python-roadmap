# Ternary Operator

raining = False
print(
    "Let's go to the", "beach" if not raining else "library"
)  # Output: Let's go to the beach

raining = True
print(
    "Let's go to the", "beach" if not raining else "library"
)  # Output: Let's go to the library
