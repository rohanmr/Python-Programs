# Write a  program to calculate the factorial of a given number. Like for 5 answer should be 120

num=int(input("Enter the no:"))

fact=1

for i in range(1,num+1):
    fact=fact * i

print(fact)



# whiteout using loop
# num=int(input("Enter the no:"))

# def fact(num):
#     if num == 0:
#         return 1
#     else:
#         return num * fact(num-1)
    

# result=fact(num)

# print(result)
