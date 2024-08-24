# Sort the array using Selection sort.

arr=[20,8,9,1,90,60,10,2,55,3,0]

def selectionSort(arr):
    n=len(arr)

    for i in range(n-1):
        mini=i

        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini=j 
        arr[i],arr[mini]= arr[mini],arr[i]


selectionSort(arr)

print(arr)