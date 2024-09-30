num=int(input("Enter the number to obtain the sum:"))

sum=0

while num > 0:
    for i in range(1,num+1):
        sum=sum+1

    num-=1
    
print("The obtained sum is:",sum)