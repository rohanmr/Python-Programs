x=int(input("Enter the 1st no:"))
y=int(input("Enter the 2nd no:"))

if x > y:
    b=y
else:
    b=x

while True:
    if b % x == 0 and b % y == 0:
        print("The LCM Of {} and {} is {}".format(x,y,b))
        break
    else:
        b=b+1

   