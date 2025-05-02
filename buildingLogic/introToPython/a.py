# # meaning=44
# # print('')
# # # if meaning>10:
# # #     print('Right on')
# # # else:
# # #     print(' Not today')
# # #terninary operator

# # print('Right on') if meaning>10 else print("Not today")

# # print(20) if meaning<20 else print(30)
# # #print( ) if condition   else print(55)

fname="Mani"
Lname="Shankar"

# print(type(fname))
# print(type(fname)==str)
# print(isinstance(fname,str))

# pizza=str("Pepporoni")
# print(type(pizza))
# print(type(pizza)==str)
# print(isinstance(pizza,str))

# fullname = fname+ " "+Lname
# print(fullname)
# fullname+="!"
# print(fullname)
# #casting a number into string
# decade=str(1980)
# print(type(decade))
# print(decade)

# statement= "i like rock music from the "+ decade +"S."
# print(statement)

# multiline='''
# hey how r u just checking in?
# o3fjom
# flckmlfcm
# kfrkfmrc        kxnxx

# '''
# print(multiline)
# sentance='I am \' master at work!\t hey! \n \n where \'s this at\\located'
# print(sentance)
# print(fname)
# print(fname.lower())
# print(fname.upper())
# print(fname)
# print(multiline.title())
# print(multiline.replace("how","good"))
# print(multiline)
# print(len(multiline))
# multiline+="       "
# print(len(multiline))
# multiline="             "+multiline
# print(len(multiline))
# print(len(multiline.strip()))
# print(len(multiline.lstrip()))
# print(len(multiline.rstrip()))


print(fname[0])
print(fname[-1])
print(fname[1:-1])
print(fname[0:])
#some methods return boolean data
print(fname.startswith("M"))
print(fname.endswith("j"))

myval=True
x= 5
print(type(myval))
print(isinstance(x,bool))

print("hello") if isinstance(x,bool) else print("hi")
import math
print(math.pi)