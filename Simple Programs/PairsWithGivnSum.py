#  Given an array A and a number X, Check any pair exists in array A which has sum exactly as X.

arr=[10, 40, 1, 2, 3, 4, 5, 7, 8, 15, 55, 30]

n=len(arr)

num=input("Enter the no to obtain the pair of sum: ")

for i in range(n):
    for j in range(i+1,n):
        if arr[i] + arr[j] == int(num):
            print([arr[i],arr[j]])
        
