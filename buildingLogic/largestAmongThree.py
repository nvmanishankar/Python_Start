def largestAmong3(inputlist):
    temp=0
    if len(initialize3numbers)!=3:
        return ("just enter 3 numbers not more than that")
    if int(inputlist[0])>int(inputlist[1]):
        temp=inputlist[0]
    else:
        temp=inputlist[1]
    if int(inputlist[2])>int(temp):
        return inputlist[2]
    else:
        return temp

print(" This to find largest among 3 number enter 3 numbers")
initialize3numbers=input("enter numbers with space between \n").split(" ")
print(initialize3numbers)
print(largestAmong3(initialize3numbers))
