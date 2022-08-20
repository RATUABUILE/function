def my(num):
    i=0
    a=[]
    b=[]
    while i<len(num):
        if num[i]==0:
            a.append(num[i])
        else:
            b.append(num[i])
        i=i+1
    c=b.extend(a)
    print(c)
my([0,1,0,3,12])