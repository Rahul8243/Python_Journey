#Given an integer n, write a program to return the factorial of n.
#  The Factorial of a number is the product of all the numbers from 1 to n.

#Note: 0 factorial is equal to 1.
#-------second method-------------

def factorial(n):
    if n == 0 or n == 1:
        return 1
 
    return n * factorial(n-1)

n = int(input('enter the number:'))
print(factorial(n))
