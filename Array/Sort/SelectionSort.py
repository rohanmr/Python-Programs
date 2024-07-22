arr=[24,17,55,75,35,88,45,22,2]

def selectionSort(arr):
    n=len(arr)

    for i in range(n-1):
        mini=i
        for j in range(i+1,n):
            if arr[j]< arr[mini]:
                mini=j
        arr[i],arr[mini]=arr[mini],arr[i]

selectionSort(arr)
print(arr)