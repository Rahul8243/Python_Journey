#Given two integers n and m (m != 0). 
# The problem is to find the number closest to n and divisible by m. 
# If there is more than one such number, 
# then output the one having the maximum absolute value.
#------------second method----------------
def closestNumber(n, m):
    remainder = n % m
    lower_multiple = n - remainder
    higher_multiple = lower_multiple + m
    
    if abs(n - lower_multiple) < abs(n - higher_multiple):
        return lower_multiple
    elif abs(n - lower_multiple) > abs(n - higher_multiple):
        return higher_multiple
    else:
        return lower_multiple if abs(lower_multiple) > abs(higher_multiple) else higher_multiple

# Example usage
print(closestNumber(-15, 6))  # Output: -18
print(closestNumber(13, 4))   # Output: 12
