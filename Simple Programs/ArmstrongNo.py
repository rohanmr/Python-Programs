# Check if a given No is Armstrong No or not ????
num=input("Enter the Number:")

sum=0

for i in num:
  sum=sum+int(i)**3

if sum == int(num):
  print("No is Armstrong")
else:
  print("No is not Armstrong")  




# num=input("Enter the no: ")

# def CheckNO(num):
#     sum=0
#     for i in num:
#         sum+=int(i)**3
        
#     if sum == int(num):
#         print("no is Armstrong")
#     else:
#         print("no is not Armstrong")
        
# CheckNO(num)