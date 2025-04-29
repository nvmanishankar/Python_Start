mani=['hello','guru','prema','kosame']
print(mani[:])
print(len(mani))
mani.append("poye mg ayyipoye")
print(mani)
mani+=['hello']
mani.extend(['shankar','jimmy'])
print(mani)
mani.insert(0,'bobby')
print(mani)
mani[2:2]=['edie','alex']
mani.remove('hello')
print(mani)
mani.remove('hello')
print(mani)
print(mani.pop())
print(mani)
del mani[0]
print(mani)
mani[1:2]=['John','Guna','BHAI']
print(mani)
mani.sort(key=str.lower)
print(mani)

mylist=list([1,'neil',2,4,5,6,8])
print(mylist)
#tupkle

mytuple=tuple(('dave',42,True))
anothertuple=('mani',21,'zero','gajini')
print(type(mytuple))
newlist=list(mytuple)
print(newlist)
newlist.append('Neil')
newtuple=tuple(newlist)
print(newtuple)
(one,*two,hey)=anothertuple
print(one)
print(two)
print(hey)
print(newtuple)