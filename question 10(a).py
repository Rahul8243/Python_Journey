#Given three numbers a, b, and c. You need to find which is the greatest of them all.

a = int(input('enter a:'))
b = int(input('enter b :'))
c = int(input('enter c : '))

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)

