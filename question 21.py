# Given an integer n find the sum of the first n natural number.
# Take input from the user
n = int(input("Enter a number: "))

# Calculate sum of first n natural numbers
total = n * (n + 1) // 2   # using the formula

# Print the result
print("Sum of first", n, "natural numbers is:", total)
