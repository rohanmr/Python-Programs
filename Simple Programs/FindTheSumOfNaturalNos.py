num=int(input("Enter the number for addition of natural numbers:"))
sum=0
while num > 0:
    for i in range(1,num+1):
        sum=sum+1
    
    num=num-1

print("The sum of natural numbers is:",sum)