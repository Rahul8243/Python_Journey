#Given a number S in the form of string, 
# the task is to find if it's divisible by 36 or not. 
# User function Template for python3

#--------------------------------------
class Solution:
    def checkDivisible36(ob, S):
        if len(S) <= 18:
            return 1 if int(S) % 36 == 0 else 0

        
        if len(S) >= 2:
            last_two = int(S[-2:])
        else:
            last_two = int(S)
        divisible_by_4 = (last_two % 4 == 0)

        # Divisible by 9: check sum of digits
        digit_sum = sum(int(d) for d in S)
        divisible_by_9 = (digit_sum % 9 == 0)

      
        if divisible_by_4 and divisible_by_9:
            return 1
        else:
            return 0

sol = Solution()
print(sol.checkDivisible36('1854'))
print(sol.checkDivisible36("288"))   
