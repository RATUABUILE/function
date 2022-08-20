def sum():
    return ra+ri
def sub():
    if ra>ri:
        print(ra-ri)
    else:
        print(ri-ra)
    # return ra-ri
def div():
    return ra%ri
def mul():
    return ra*ri
ra=int(input("enter any number:"))
ri=int(input("enter any number:"))
o=input("enter any operator:")
def my():
    if o=="+":
        print(sum())
    elif o=="-":
        sub()
    elif o=="%":
        print(div())
    elif o=="*":
        print(mul())
my()