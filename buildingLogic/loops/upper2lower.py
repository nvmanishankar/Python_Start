a=input("Enter a word to covert upper 2 lower: ")

for i in a:
    if i.lower() != i:
        a=a.replace(i,i.lower())
print(a)

#if not this we can take an empty string and add the lower case letters to it