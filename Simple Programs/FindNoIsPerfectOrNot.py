num=int(input("Enter the number: "))

def perfectNo(num):
    sum=0
    for i in range(1,num):
        if num % i == 0:
            sum=sum+i
    
    if sum == num:
        print("Entered no is perfect")
    else:
        print("enter no is not a perfect no")

perfectNo(num)