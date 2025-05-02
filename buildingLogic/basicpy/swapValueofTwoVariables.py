def swapValueofTwoVariables(a,b):
    # This function swaps the values of two variables without using a third variable
    # Get the values of the two variables from the user
    a,b=b,a
    return a,b





fVariable=int(input("Enter the First Variable:"))
SVariable=int(input("Enter The Second Variable:"))

print(f"Before Swapping: First Variable: {fVariable}, Second Variable: {SVariable}")
fVariable,SVariable=swapValueofTwoVariables(fVariable,SVariable)   
print(f"After Swapping: First Variable: {fVariable}, Second Variable: {SVariable}")

#For above i have used "fstring" method which is used to string formatting and better to use.