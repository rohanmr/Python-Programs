# Sort the array using Selection sort.

arr=[20,8,9,1,90,60,10,2,55,3,0,4]

#Function to sort array by using selectionSort

def selectionSort(arr):
    # Calculate the length of array
    n=len(arr)

    for i in range(n):
        mini=i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini=j
        
        # Swapping the element of array
        arr[mini],arr[i]=arr[i],arr[mini]


selectionSort(arr)

print("Your Sorted array is:",arr)