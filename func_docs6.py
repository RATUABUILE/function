def alphabets(string):
    i=0
    count_upper=0
    count_lower=0
    while i<len(string):
        if string[i]>="a" and string[i]<="z":
            count_lower=count_lower+1
        else:
            count_upper=count_upper+1
        i+=1
    print(count_upper)
    print(count_lower)
string=input("enter string:")
alphabets(string)