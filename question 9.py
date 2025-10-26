#Given a positive integer n, determine whether it is odd or even. 
# Return true if the number is even and false if the number is odd.

class Solution:
    def isEven(self,n):
        if n % 2 == 0:
            return True
        else:
            return False
        
sol = Solution()
print(sol.isEven(4))
print(sol.isEven(7))