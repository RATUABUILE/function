# PART_1
# def perfect():
#     num=int(input("enter the number:"))
#     i=1
#     sum=0
#     while i<num:
#         if num%i==0:
#             sum=sum+i
#         i+=1
#     if sum==num:
#         print("perfect number")
#     else:
#         print("not perfect number")

# PART_2
def perfect(n):
    i=1
    while i<=n:
        j=1
        sum=0
        while j<i:
            if i%j==0:
                sum=sum+j
            j+=1
        if sum==i:
            print(i)
        i+=1
perfect(1000)