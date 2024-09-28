num =int(input("Enter the no:"))

sum=0

while num > 0:
    for i in range(1,num+1):
        sum=sum+i
    
    num=-1

print("Sum of the natural numbers are:",sum)