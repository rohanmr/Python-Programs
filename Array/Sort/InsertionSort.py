# Sort the array using insertion sort.

arr=[40,10,50,60,80,90,30,70,20]

def insertionSort(arr):
    n=len(arr)

    for i in range(1,n):
        key=arr[i]
        j=i-1

        while j>=0 and key < arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

insertionSort(arr)
print(arr)