# find the sum of all element of list 

myList=[20,40,80,90,30,70,60,10]

n=len(myList)

total=0

for i in range(0,n):
    total=total+myList[i]

print("Sum of list elements are: ",total)