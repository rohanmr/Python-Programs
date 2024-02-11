
arr=[10,20,30,40,50,60,70]
target=70

def binarySearch(arr,target):
    left,right=0,len(arr)-1

    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return arr[mid]
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1

result=binarySearch(arr,target)

print(result)