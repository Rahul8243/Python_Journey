#Given an integer n, write a program to return the factorial of n.
#  The Factorial of a number is the product of all the numbers from 1 to n.

#Note: 0 factorial is equal to 1.

n = int(input('enter number:'))

fact = 1

for i in range(1 , n + 1):
    fact *= i

print(fact)
