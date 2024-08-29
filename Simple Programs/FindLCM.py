# LCM of Two No "Least Common Multiple"

x=int(input("Enter the first no: "))
y=int(input("Enter the second no: "))

if x > y :
    b = x
else:
    b = y

while True:
    if b % x == 0  and b % y == 0:
        print("The LCM of {} and {} is {}".format(x,y,b))
        break
    else:
        b=b+1 
