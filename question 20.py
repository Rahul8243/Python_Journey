# Given two numbers a and b, you need to swap their
# values so a holds the value of b and b holds the value of a. Just write the code 
# to swap values of a and b at the specified place.

# Take inputs
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Swap the values
a, b = b, a

# Print the swapped values
print("After swapping:")
print("a =", a)
print("b =", b)
