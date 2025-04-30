#we can use functons to covert data into tuples and dictionaries 


def multidata(*args):
    #this fuction takes multiple arguments and returns them as tuplke
    return args
def multidata2(**kwargs):
    #this function takes multiple keyword arguments and returns them as dictionary
    return kwargs
def multidata3(*args, **kwargs):    
    #this function takes multiple arguments and keyword arguments and returns them as tuple and dictionary
    return args, kwargs
multidata=multidata(1,2,3,4,5)
multidata2=multidata2(name="John", age=30, city="New York") 
multidata3=multidata3(1,2,3,4,5,name="John", age=30, city="New York")
print(multidata)
print(multidata2)
print(multidata3)
print(type(multidata))
print(type(multidata2))
print(type(multidata3))