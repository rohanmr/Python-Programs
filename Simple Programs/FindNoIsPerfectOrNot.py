# It's a positive integer the sum of all its factors is equal to the number the this is a perfect number
num=int(input("Enter the no :"))

sum=0

for i in range(1,num):
    if num % i == 0:
        sum=sum+i


if sum == num:
    print("Entered number is perfect number")
else:
    print("Entered number is not perfect")






# num=int(input("Enter the number: "))

# def perfectNo(num):
#     sum=0
#     for i in range(1,num):
#         if num % i == 0:
#             sum=sum+i
    
#     if sum == num:
#         print("Entered no is perfect")
#     else:
#         print("enter no is not a perfect no")

# perfectNo(num)




