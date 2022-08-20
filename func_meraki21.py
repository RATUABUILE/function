first=input("enter the string:")
second=input("enter the string:")
def string(first,second):
    if len(first)>len(second):
        print(first)
    elif len(second)>len(first):
        print(second)
    elif len(first)==len(second):
        print(first)
        print(second)
string(first,second)