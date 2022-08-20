list= [3, 5, 7, 34, 2, 89, 2, 5]
def max(list):
    i=0
    max=list[0]
    while i<len(list):
        if list[i]>max:
            max=list[i]
        i+=1
    return max
print(max(list)) 