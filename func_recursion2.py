def table(number,i):
    print(number,"*",i,"=",number*i)
    if i<10:
        table(number,i+1)
i=int(input("enter initialization:"))
number=int(input("enter the number"))
table(number,i)