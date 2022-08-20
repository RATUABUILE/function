def sum(list):
    i=0
    sum=0
    while i<len(list):
        sum=sum+list[i]
        i+=1
    return sum
list=[8,2,3,0,7]
print(sum(list))