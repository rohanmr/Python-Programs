# Write a program to make a pyramid pattern with numbers increased by 1.
#     1 
#   2 3 
#  4 5 6 
# 7 8 9 10 

num=4
n=1

for i in range(1,num+1):
    for j in range(num-i):
        print(" ",end="")
    
    for j in range(1,i+1):
        print(n,end=" ")
        n=n+1
    print()
