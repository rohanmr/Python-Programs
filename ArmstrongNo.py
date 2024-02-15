num=input("Enter number:")
sum=0

for i in num:
    sum+=int(i)**3

if sum == int(num):
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")