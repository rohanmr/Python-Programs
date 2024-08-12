# 1.Find out the minimum and maximum of three numbers
x=int(input("Enter the 1st no: "))
y=int(input("Enter the 2nd no: "))
z=int(input("Enter the 3rd no: "))

if x > y and  x > z:
    print("Max",x)
elif y > x and y > z:
    print("Max", y)
else:
    print("Max",z)

if x < y and x < z:
    print("Min",x)
elif y < x and y < z :
    print("Min",y)
else:
    print("Min",z)

    