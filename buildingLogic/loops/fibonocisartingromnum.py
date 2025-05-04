#fibonocistarting from any two numbers
#fibonci is nothing but sum of previous two  numbers 

#startinf from 1,1,2,3,5,8,13,21,24
#logic for this 

# import sys
# X=[1,1]
# a=int(input("Enter a number: "))
# b=int(input("Enter a number: "))


# for i in range(b):
#     c=X[i]+X[i+1]
#     X.append(c)
#     if c>=a and c<=b:
#         print("Fibonacci number is",c)
#     if c<a:
#         print("Fibonacci number is",c)
   
#     if c>=b:
       
#         sys.exit()

#above is my approach but i got better approch than this

# i will use while loop


a=int(input("Enter the Lower limit: "))
b=int(input("Enter the Upper limit: "))

f1,f2=1,1

i=0

while f2 <= b:
    if f2 >= a:
        print("Fibonacci number is", f2)
    
    f1, f2 = f2, f1 + f2

