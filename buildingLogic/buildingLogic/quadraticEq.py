
import math
A=input("Enter values of quadratic eQ").split(" ")
a=int(A[0])
b=int(A[1])
c=int(A[2])
print((-b+math.sqrt(b^2-4*a*c))/2*a)
print((-b-math.sqrt(b^2-4*a*c))/2*a)