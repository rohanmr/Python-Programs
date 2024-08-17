# Write a program to make such a pattern like a right angle triangle with the number increased by 1. The pattern like :
#    1
#    2 3
#    4 5 6
#    7 8 9 10

n=5
num=1

for i in range(n-1):
    for j in range(i+1):
        print(num,end=" ")
        num=num+1
    print()