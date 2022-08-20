n=int(input("Enter the input:"))
i=0
while i<n:
    z=int(input("Enter the battery percentage:"))
    if z<=15:
        print("Low Battery")
    else:
        print("NO")
    i=i+1