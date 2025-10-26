#Given two integers n and m (m != 0). 
# The problem is to find the number closest to n and divisible by m. 
# If there is more than one such number, 
# then output the one having the maximum absolute value.
#------------first method----------------
class Solution:
    def closest_num(self,n,m):
        quotient = n // m
        lower = m * quotient
        higher = m * (quotient + 1) if n * m > 0 else m *(quotient - 1)

        if abs(n- lower) < abs(n - higher):
            return lower
        elif abs(n - higher) < abs(n - lower):
            return higher
        else:
            return lower if abs(n-lower) > abs(higher) else higher
        
sol = Solution()
print(sol.closest_num(13,4))
print(sol.closest_num(15,4))
