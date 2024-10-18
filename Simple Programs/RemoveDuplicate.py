arr= [1, 2, 2, 3, 4, 4, 5]


def removeDuplicate(arr):
    return list(set(arr))

print("your original array is:",arr)

result=removeDuplicate(arr)

print("Your new array is:",result)