#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ONLINE ORDER PLACING SYSTEM:-
cf45=0
cf48=0
cf50=0
cf52=0
cf55=0
cf58=0
cf60=0
cf95=0
cf100=0
f_45=0
f_48=0
f_50=0
f_52=0
f_55=0
f_58=0
f_60=0
f_95=0
f_100=0
a=input("Enter your name : ")
print()
print("HELLO!",a,"WELCOME TO RAYMOND_WORLD!")
print()
print("Choose the category :- ")
print()
b="Pure Cotton________________45/48/50"
c="Mix Cotton_________________52/55"
d="Synthetic__________________58/60"
e="Silk_______________________95/100"
print("1",b)
print("2",c)
print("3",d)
print("4",e)
print()
f=int(input("Enter the serial number of category : "))
print()
if f==1:
    print("Select the quality of Cotton : ")
    print("1___Rs.45/Mtr.")
    print("2___Rs.48/Mtr.")
    print("3___Rs.50/Mtr.")
    print()
    f45=int(input("Enter the serial number of quality : "))
    print()
    if f45==1:
        f_45=int(input("Quantity (in mtrs.): "))
        print()
        print("Want to buy other qualities in Cotton ?")
        print("Type 1 for 'YES'")
        print("Type 2 for 'NO'")
        more1=int(input())
        print()
        if more1==1:
            print("1___Rs.45/Mtr.")
            print("2___Rs.48/Mtr.")
            print("3___Rs.50/Mtr.")
            f48=int(input("Enter the serial number of quality : "))
            print()
            if f48==2:
                f_48=int(input("Quantity (in mtrs.): "))
                print()
                print("Want to buy other qualities in Cotton ?")
                print("Type 1 for 'YES'")
                print("Type 2 for 'NO'")
                more2=int(input())
                print()
                if more2==1:
                    print("1___Rs.45/Mtr.")
                    print("2___Rs.48/Mtr.")
                    print("3___Rs.50/Mtr.")
                    f50=int(input("Enter the serial number of quality : "))
                    print()
                    if f50==3:
                        f_50=int(input("Quantity (in mtrs.): "))
    elif f45==2:
        f_48=int(input("Quantity (in mtrs.): "))
        print()
        print("Want to buy other qualities in Cotton ?")
        print("Type 1 for 'YES'")
        print("Type 2 for 'NO'")
        more2=int(input())
        print()
        if more2==1:
            print("1___Rs.45/Mtr.")
            print("2___Rs.48/Mtr.")
            print("3___Rs.50/Mtr.")
            f50=int(input("Enter the serial number of quality : "))
            print()
            if f50==3:
                f_50=int(input("Quantity (in mtrs.): "))
                print()
                print("Want to buy other qualities in Cotton ?")
                print("Type 1 for 'YES'")
                print("Type 2 for 'NO'")
                more1=int(input())
                print()
                if more1==1:
                    print("1___Rs.45/Mtr.")
                    print("2___Rs.48/Mtr.")
                    print("3___Rs.50/Mtr.")
                    print()
                    f45=int(input("Enter the serial number of quality : "))
                    print()
                    if f45==1:
                        f_45=int(input("Quantity (in mtrs.): "))
    elif f45==3:
        f_50=int(input("Quantity (in mtrs.): "))
        print()
        print("Want to buy other qualities in Cotton ?")
        print("Type 1 for 'YES'")
        print("Type 2 for 'NO'")
        more2=int(input())
        print()
        if more2==1:
            print("1___Rs.45/Mtr.")
            print("2___Rs.48/Mtr.")
            print("3___Rs.50/Mtr.")
            f48=int(input("Enter the serial number of quality : "))
            print()            
            if f48==2:
                f_48=int(input("Quantity (in mtrs.): "))
                print()
                print("Want to buy other qualities in Cotton ?")
                print("Type 1 for 'YES'")
                print("Type 2 for 'NO'")
                more2=int(input())
                print()
                if more2==1:
                    print("1___Rs.45/Mtr.")
                    print("2___Rs.48/Mtr.")
                    print("3___Rs.50/Mtr.")
                    f45=int(input("Enter the serial number of quality : "))
                    print()
                    if f45==1:
                        f_45=int(input("Quantity (in mtrs.): "))
    elif f45==2:
        f_48=int(input("Quantity (in mtrs.): "))
        print()
        print("Want to buy other qualities in Cotton ?")
        print("Type 1 for 'YES'")
        print("Type 2 for 'NO'")
        more2=int(input())
        print()
        if more2==1:
            print("1___Rs.45/Mtr.")
            print("2___Rs.48/Mtr.")
            print("3___Rs.50/Mtr.")
            f45=int(input("Enter the serial number of quality : "))
            print()            
            if f45==1:
                f_45=int(input("Quantity (in mtrs.): "))
                print()
                print("Want to buy other qualities in Cotton ?")
                print("Type 1 for 'YES'")
                print("Type 2 for 'NO'")
                more2=int(input())
                print()
                if more2==1:
                    print("1___Rs.45/Mtr.")
                    print("2___Rs.48/Mtr.")
                    print("3___Rs.50/Mtr.")
                    f50=int(input("Enter the serial number of quality : "))
                    print()
                    if f50==1:
                        f_50=int(input("Quantity (in mtrs.): "))
    elif f45==3:
        f_50=int(input("Quantity (in mtrs.): "))
        print()
        print("Want to buy other qualities in Cotton ?")
        print("Type 1 for 'YES'")
        print("Type 2 for 'NO'")
        more2=int(input())
        print()
        if more2==1:
            print("1___Rs.45/Mtr.")
            print("2___Rs.48/Mtr.")
            print("3___Rs.50/Mtr.")
            f48=int(input("Enter the serial number of quality : "))
            print()            
            if f48==1:
                f_45=int(input("Quantity (in mtrs.): "))
                print()
                print("Want to buy other qualities in Cotton ?")
                print("Type 1 for 'YES'")
                print("Type 2 for 'NO'")
                more2=int(input())
                print()
                if more2==1:
                    print("1___Rs.45/Mtr.")
                    print("2___Rs.48/Mtr.")
                    print("3___Rs.50/Mtr.")
                    f45=int(input("Enter the serial number of quality : "))
                    print()
                    if f45==2:
                        f_48=int(input("Quantity (in mtrs.): "))
    elif f45==1:
        f_45=int(input("Quantity (in mtrs.): "))
        print()
        print("Want to buy other qualities in Cotton ?")
        print("Type 1 for 'YES'")
        print("Type 2 for 'NO'")
        more2=int(input())
        print()
        if more2==1:
            print("1___Rs.45/Mtr.")
            print("2___Rs.48/Mtr.")
            print("3___Rs.50/Mtr.")
            f48=int(input("Enter the serial number of quality : "))
            print()            
            if f48==3:
                f_50=int(input("Quantity (in mtrs.): "))
                print()
                print("Want to buy other qualities in Cotton ?")
                print("Type 1 for 'YES'")
                print("Type 2 for 'NO'")
                more2=int(input())
                print()
                if more2==1:
                    print("1___Rs.45/Mtr.")
                    print("2___Rs.48/Mtr.")
                    print("3___Rs.50/Mtr.")
                    f45=int(input("Enter the serial number of quality : "))
                    print()
                    if f45==2:
                        f_48=int(input("Quantity (in mtrs.): "))
                        
elif f==2:
    print("Select the quality of Mix Cotton : ")
    print("1__Rs.52/Mtr.")
    print("2___Rs.55/Mtr.")
    print()
    f52=int(input("Enter the number of quality : "))
    print()
    if f52==1:
        f_52=int(input("Quantity (in mtrs.): "))
        print()
        print("Want to buy other qualities in Mix Cotton ?")
        print("Type 1 for 'YES'")
        print("Type 2 for 'NO'")
        more1=int(input())
        print()
        if more1==1:
            print("1___Rs.52/Mtr.")
            print("2___Rs.55/Mtr.")
            f55=int(input("Enter the serial number of quality : "))
            print()
            if f55==1:
                f_55=int(input("Quantity (in mtrs.): "))
                print()
    elif f52==2:
        f_52=int(input("Quantity (in mtrs.): "))
        print()
        print("Want to buy other qualities in Mix Cotton ?")
        print("Type 1 for 'YES'")
        print("Type 2 for 'NO'")
        more1=int(input())
        print()
        if more1==1:
            print("1___Rs.52/Mtr.")
            print("2___Rs.55/Mtr.")
            f55=int(input("Enter the serial number of quality : "))
            print()
            if f55==1:
                f_55=int(input("Quantity (in mtrs.): "))
                print()
elif f==3:
    print("Select the quality of Synthetic : ")
    print("1__Rs.58/Mtr.")
    print("2___Rs.60/Mtr.")
    print()
    f58=int(input("Enter the serial number of quality : "))
    print()
    if f58==1:
        f_58=int(input("Quantity (in mtrs.): "))
        print()
        print("Want to buy other qualities in Synthetic ?")
        print("Type 1 for 'YES'")
        print("Type 2 for 'NO'")
        more1=int(input())
        print()
        if more1==1:
            print("1___Rs.58/Mtr.")
            print("2___Rs.60/Mtr.")
            f60=int(input("Enter the serial number of quality : "))
            print()
            if f60==1:
                f_60=int(input("Quantity (in mtrs.): "))
                print()
    elif f58==2:
        f_58=int(input("Quantity (in mtrs.): "))
        print()
        print("Want to buy other qualities in Synthetic?")
        print("Type 1 for 'YES'")
        print("Type 2 for 'NO'")
        more1=int(input())
        print()
        if more1==1:
            print("1___Rs.58/Mtr.")
            print("2___Rs.60/Mtr.")
            f60=int(input("Enter the serial no. of quality : "))
            print()
            if f60==1:
                f_60=int(input("Quantity (in mtrs.): "))
                print()
elif f==4:
    print("Select the quality of Silk : ")
    print("1__Rs.95/Mtr.")
    print("2___Rs.100/Mtr.")
    print()
    f95=int(input("Enter the serial number of quality : "))
    print()
    if f95==1:
        f_95=int(input("Quantity (in mtrs.): "))
        print()
        print("Want to buy other qualities in Silk ?")
        print("Type 1 for 'YES'")
        print("Type 2 for 'NO'")
        more1=int(input())
        print()
        if more1==1:
            print("1___Rs.95/Mtr.")
            print("2___Rs.100/Mtr.")
            f100=int(input("Enter the serial number of quality : "))
            print()
            if f100==1:
                f_100=int(input("Quantity (in mtrs.): "))
                print()
    elif f95==2:
        f_95=int(input("Quantity (in mtrs.): "))
        print()
        print("Want to buy other qualities in Silk ?")
        print("Type 1 for 'YES'")
        print("Type 2 for 'NO'")
        more1=int(input())
        print()
        if more1==1:
            print("1___Rs.95/Mtr.")
            print("2___Rs.100/Mtr.")
            f100=int(input("Enter the serial number of quality : "))
            print()
            if f100==1:
                f_200=int(input("Quantity (in mtrs.): "))
                print()
print("Enter your shipping address")
address=input()
cf45+=f_45*45
cf48+=f_48*48
cf50+=f_50*50
cf52+=f_52*52
cf55+=f_55*55
cf58+=f_58*58
cf60+=f_60*60
cf95+=f_95*95
cf100+=f_100*100
Total = cf45+cf48+cf50+cf52+cf55+cf58+cf60+cf95+cf100
print()
print("Please choose your payment method")
print()
print("1___UPI")
print("2___NET Banking")
method=int(input())
if method==1:
    print("UPI Application will be opened")
elif method==2:
    print("Banking Application will be opened")
print()
print("Shipping to:",address)
print("Total:                 ",Total)
print("Delivery charges:       7999")
total_with_delivery=Total + 7999
print("Order Total:           ",total_with_delivery)
print("Enter 1 to place your order")
Placed=int(input())
if Placed==1:
    print("Your order is placed successfully")
    print("THANKS FOR SHOPPING WITH US !! ")
else:
    print("order again!")







