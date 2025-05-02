def add_1(num):
    if (num>=9):
        return num+1
    total=num+1
    print(total)
    return add_1(total)
add_1(0)


