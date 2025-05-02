# #lambda.py 
# #lambda function is a single expression which returns a value
# squared=lambda num:num*num
# print(squared(5))

# addTwo=lambda num:num+2
# print(addTwo(5))

# sum=lambda a,b:a+b
# print(sum(5,10))

# ##########################

# def func(x):
#     return lambda num:num+x
# addTen=func(10)

# addTwenty=func(20)
# print(addTen(8))

#map function takes first arugument as a fuction

# def square(num):
#     return num*num

numbers=[1,2,3,4,5,1]
# sqared_nums=map(square,numbers)
# print(list(sqared_nums))


# lambda num:num %2 !=0
# odd_numbers=map(lambda num:num %2 !=0,numbers)
# print(list(odd_numbers))

#differance between map and filter filter only returns true and map returns all

from functools import reduce


total=reduce(lambda acc,crr:acc+crr,numbers)
print(total)