t=int(input("enter the number :"))
l=int(input("enter the number :"))
i=t
c=0
while i<=l:
    k=i%10
    if k==2 or k==3 or k==9:
        c=c+1
    i+=1
print(c)