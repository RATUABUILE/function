def speed_of_driver(speed):
    if speed<70:
        print("70")
    else:
        speed1=speed-70
        point=speed1//5
        if point<=12:
            print("point is",point)
        else:
            print("point",point,"-" ",","license suspended")
speed=int(input("enter the number:"))
speed_of_driver(speed)