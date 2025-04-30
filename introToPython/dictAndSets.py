#dictionaries
band={
    "vocals":"Plant",
    "guitar":"Page"
}
#using constuctor func
band2=dict(vocals="Plant",guitar="page")
print(band)
print(band2)
print(type(band))
print(len(band))
#acces items
print(band["guitar"])
print(band.get("guitar"))
print(band.keys())
print(band.values())
print(list(band.items()))

print("guita" in band)

#change values
band["vocals"]="coverdale"
band.update({"bass":"jpg"})
print(band.pop("vocals"))
print(band)
band["drums"]="bonaam"
print(band)
print(band.popitem())
print(band)
# #delete or clear 
band["drums"]="bonaam"
del band["drums"]
print(band)
band2.clear()
print(band2)
del band2
# copy dicts
band2= band # creates a referance both refering to same dict in memory
print("bad copy")

band2=band.copy()
print(band2)
print(band)
band2["druns"]="guns"
print(band)
print(band2)
band3=dict(band)
print(band3)



#NestedDictionaries

member1={
    "name":"plant",
    "instrument":"disc"
}
member2={
    "name":"godzilaa",
    "instrument":"siren"
}
disc4={
    "member1":member1,
    "member2":member2
}
print(disc4)
print(disc4["member1"]["name"])

#sets\\
nums={1,2,3,4}
nums1=set((1,2,3,4))
print(nums)
print(nums1)
print(type(nums))
print(len(nums))
#no duplicates allowed
nums={1,2,3,3,4,3,3,3,3,3,45,7,4,3}
print(2 in nums)
#we cannot any specifc value based on index 
#adding a new element into set.
nums.add(8)
print(nums)
morenums={5,6,7}
nums.update(morenums)
print(nums)
#you can use update with lists ,tuples and didctionaries

#merge two sets with a list

one={1,2,3}
two={5,6,7}
mynewset=one.union(two)
print(mynewset)
one={1,2,3}
two={2,3,5,6,7}
one.intersection_update(two)
print(one)