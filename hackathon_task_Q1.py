def divisibility(n):
    i=0
    a=[]
    while i<n:
        n1=int(input("enter the number:"))
        a.append(n1)
        j=0
        b=""
        while j<len(a):
            z=a[j]%10
            b=b+str(z)
            c=int(b)
            j+=1
        i+=1
    if c%10==0:
        print("yes")
    else:
        print("no ")
n=int(input("enter the number:"))
divisibility(n)