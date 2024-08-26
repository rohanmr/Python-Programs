# Sort the array using Bubble sort.

arr=[20,60,80,70,10,90,50,40,30]

def bubbleSort(arr):
    n=len(arr)
    
    for i in range(n-1):
        swapped=False
        
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
                
        if not swapped:
            break
        
        
bubbleSort(arr)
print(arr)


