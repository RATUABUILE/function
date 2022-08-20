av=10
def count(x):
    i=1
    while i<=x:
        if i>av:
            print("out of stock")
            continue
        print("chocolates")
        i+=1
x=int(input("how many chocolates you want?:"))
count(x)