def even_and_odd(n):
    i=0
    while i<=n:
        if i%2==0:
            print(i,"even")
        else:
           print(i,"odd")
        i+=1
n=int(input("enter the number:"))
even_and_odd(n)