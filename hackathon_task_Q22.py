def my():
    user=input("enter the string")
    c=list(user)
    l=len(c)
    i=-1
    a=[]
    while i>=-l:
        a.append(c[i])
        i=i-1
    if a==c:
        print("true")
    else:
        print("false")
    return a
my()