from math import factorial


x  = int(input())
n  = int(input())

total = 1

for i in range(1,n+1):
    total += x/factorial(i)

print(total)