#xlousre is a function having acces to the  scope of its parent
# afunction after parent function has returned

def parent_function(person):
    coins=3
    def play_gane():
        nonlocal coins
        coins -=1
        if coins>0:
            print("\n" +person +"has" + str(coins)+" coins left")
        elif coins==0:
            print("\n" +person +"has no coins left")
        else:
            print("\n" +person +"has no coins left")
    return play_gane
tommy=parent_function("Tommy")
print(tommy)
tommy()
tommy()