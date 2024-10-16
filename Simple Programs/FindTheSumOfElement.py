# find the sum of all element of list 

myList=[20,40,80,90,30,70,60,10,50]

# n=len(myList)

# total=0

# for i in range(0,n):
#     total=total+myList[i]

# print("Sum of list elements are: ",total)


def addArrayOfNumbers(myList):
    n=len(myList)
    sum=0

    for i in range(0,n):
        sum=sum+myList[i]

    return sum

result=addArrayOfNumbers(myList)

print(result)

    