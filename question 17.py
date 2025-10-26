#Strong Numbers are the numbers whose sum of factorial of digits is equal to the original number.
#  Given a number N, the task is to check if it is a Strong Number or not.
#  Print 1 if the Number is Strong, else Print 0

#----------------------------

class Solution:
    def is_Strong(self,N):
        def factorial(n):
            fact = 1
            for i in range(1, n+1):
                fact *= i
            return fact
        
        original = N
        sum_fact = 0

        while N > 0:
            digit = N % 10
            sum_fact += factorial(digit)
            N //=10
        return 1 if sum_fact == original else 0

sol = Solution()
print(sol.is_Strong(145))
print(sol.is_Strong(125))