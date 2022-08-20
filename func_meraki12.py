# PART_1
# def calculator(numberx,numbery,operation):
#     if operation=="add":
#         number1=numberx+numbery
#         return(number1)
#     elif operation=="substract":
#         number2=numberx-numbery
#         return(number2)
#     elif operation=="multiply":
#         number3=numberx*numbery
#         return(number3)
#     else:
#         number4=numberx/numbery
#         return(number4)
# print("addition of two numbers:",calculator(20,25,"add"))
# print("substract of two numbers:",calculator(40,3,"substract"))
# print("multiply of two numbers:",calculator(10,4,"multiply"))
# print("division of two numbers:",calculator(40,4,"divide"))

# PART_2
# def calculator(num1,num2):
#     return calculator
# num1=int(input("enter the number:"))
# num2=int(input("enter the number:"))
# add_result=(num1+num2)
# print("sum:",add_result)
# substract_result=(num1-num2)
# print("difference:",substract_result)
# multiply_result=(num1*num2)
# print("product:",multiply_result)
# divide_result=(num1/num2)
# print("divide:",divide_result)

# PART_3
# def list_change(list1,list2):
#     i=0
#     a=[]
#     while i<len(list1):
#         list1.extend(list2)
#         i+=1
#     print(list1)
# list_change([5,10,50,20],[2,20,3,5])

def fun(list1,list2):
    list1.extend(list2)
    print(list1)
fun([5,10,50,20],[2,20,3,5])