from math import factorial


num = int(input())
total =1
for x in range(1,num+1):
   total += 1/factorial(x)

print(total)