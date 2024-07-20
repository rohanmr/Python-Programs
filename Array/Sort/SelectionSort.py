arr=[24,17,66,45,33,22]

def selectionSort(arr):
    n=len(arr)
    for i in range(n-1):
        mini=i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini=j
            
            if mini!=i:
                arr[i],arr[mini]=arr[mini],arr[i]

selectionSort(arr)

print(arr)