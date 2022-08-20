def squares(numbers):
    i=1
    while i<=numbers:
        print(i,":",i**2,end=",")
        i+=1
numbers=int(input("enter the number"))
squares(numbers)
print()