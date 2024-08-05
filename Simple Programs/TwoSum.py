# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

num=[0,1,2,3,4,5,10,90,60,40,20]

target=int(input("Enter the no: "))

n=len(num)

for i in range(n):
    for j in range(i+1,n):
        if num[i]+num[j]==target:
            x=[i,j]
            print(x)

