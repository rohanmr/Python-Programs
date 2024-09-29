# Search a no by using linear search .

arr=[10,50,70,90,60,30,20,40]
target=int(input("Enter the no: "))

def LinearSearch(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return arr[i]
                
result=LinearSearch(arr,target)
print("This is your Search element is:",result)




# arr=[20,40,50,70,90,60,30]

# target=int(input("Enter the no:"))

# def linearSearch(arr,target):
#     for i in range(len(arr)):
#         if arr[i]==target:
#             return arr[i]
#     else:
#         print("No is not in the array")
        



# result=linearSearch(arr,target)


# print("Your searched no is",result)
