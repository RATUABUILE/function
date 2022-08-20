def unique(list):
    i=0
    a=[]
    while i<len(list):
        if list[i] not in a:
            a.append(list[i])
        i+=1
    print(a)
unique([1,2,1,3,3,3,4,5])