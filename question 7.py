# @param x: int
# @return: string

def checkOddEven(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(checkOddEven(2))
print(checkOddEven(7))
print(checkOddEven(14))