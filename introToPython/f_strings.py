person="Dave"
coins=3

print("/n"+person+ str(coins) +" coins left for next game")

message="\n %s has %d coins left." %(person,coins)
message="\n %s has %d coins left." %(person,coins)
print(message)
#format method approaches
message="\n{} has {} coins left.".format(person,coins)
print(message)
message="\n{1} has {0} coins left.".format(person,coins)
print(message)
message = "\n {person} has {coins} coins left".format(coins=coins,person=person)
print(message)
message = "\n {person} has {coins} coins left".format(coins=coins,person=person)
print(message)

player={"person":person,"coins":coins}

message="\n {person} has {coins} coins lrft.".format(**player)

print(message)

#fstrings!This how its done

message=f"\n {person.upper()} has {5+4} coins left"
print(message)

message= f"\n {player['person'].upper()} has {player['coins']+4} coins left"
print(message)

num=10

print(f"\n 2.25 times {num} is {2.25*num:.2f} ")
print(f"\n {num} is {'odd' if num%2!=0 else 'even'}")

for i in range(1,11):
    print(f"\n {i} divided by 4.52 is {i/4.52:.2%}")
