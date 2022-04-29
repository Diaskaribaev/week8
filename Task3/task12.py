from math import factorial


x  = int(input())
n  = int(input())

total = x

for i in range(2,n+1):
    if i%2>0:
        total += x/factorial(i) 
    elif i%2==0:
        total -= x/factorial(i) 



print(total)