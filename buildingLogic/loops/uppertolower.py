PascalRows=int(input())
out=[]
for i in range(1,PascalRows+1):
    x=[]
    for j in range(i):
        if j==0 or j==i-1:
            x.append(1)
        else:
            #this logic for middle elements
            x.append(out[i-2][j-1]+out[i-2][j])

    out.append(x)
print(out)
#this is my first leetcode problem but i used loops to do it its more timecomplexcity and space complexity than other but this is my present approch feeling good.