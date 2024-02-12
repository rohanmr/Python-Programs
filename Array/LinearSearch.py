
arr=[10,50,70,90,60,30,20,40]
target=90

def LinearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i]==target:
            return arr[i]
        
result=LinearSearch(arr,target)
print(result)