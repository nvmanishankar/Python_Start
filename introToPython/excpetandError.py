
class justnotcoolerror(Exception):
    pass




x="jfdvjn"
try:
    # if not type(x) is int:
    #     raise TypeError("x must be an integer")
    raise   justnotcoolerror("this is a custom error")
except NameError:
    print("there is an error")
except ZeroDivisionError:
    print("cannot divide by zero")
except Exception as error:
    print(error)
else:
    print("no error")
finally:
    print("this will always run")   