x=int(input("enter no. of 10 rupees coin:"))
y=int(input("enter no. of 5 rupees coin:"))
if x>0 and y>0:
    ten=x*10
    five=y*5
    total_amount=ten+five
    print(total_amount)
elif x>0 and y<=0:
    print(x*10)
elif x<=0 and y>0:
    print(y*5)