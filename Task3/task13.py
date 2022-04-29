from math import factorial


x  = int(input())
n  = int(input())

total = x 

for i in range(1,n+1):
    if i%2>0:
        total -= x/factorial(2*i+1) 
    elif i%2==0:
        total += x/factorial(2*i+1) 



print(total)
