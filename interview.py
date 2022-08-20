def vaccination():
    person=int(input("enter the age:"))
    if person>=18:
        print("can vacinate")
        dose=input("enter doses:")
        if dose=="first_dose":
            print("can take second_dose")
        elif dose=="second_dose":
                print("congratulation you have complete the doses")
        elif dose=="none":
            print("Go for first dose")
    else:
        print("cannot vaccinate")
vaccination()