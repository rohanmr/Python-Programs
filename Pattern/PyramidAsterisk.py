# Write a  program to make such a pattern as a pyramid with an asterisk.
#    * 
#   * * 
#  * * * 
# * * * *


num=int(input("Enter the no:"))
n="*"

for i in range(num-1):
    for j in range(i,num):
        print(" ",end="")
    for j in range(i+1):
        print(n,end=" ")
    
    print()






# for i in range(1,num+1):
#     for j in range(i,num):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print(n,end=" ")
#     print()


