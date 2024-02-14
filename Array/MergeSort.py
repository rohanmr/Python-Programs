
arr=[12,55,6,1,2,77,44,66,20,10,78,4,3,99]

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2

    left_half=arr[:mid]
    right_half=arr[mid:]
    left_half=merge_sort(left_half)
    right_half=merge_sort(right_half)
    return merge(left_half,right_half)

def merge(left,right):
    new=[]
    i,j=0,0

    while i < len(left)  and j < len(right):
        if left[i]<right[j]:
            new.append(left[i])
            i+=1
        else:
            new.append(right[j])
            j+=1
    new.extend(left[i:])
    new.extend(right[j:])
    return new



sorted_arr=merge_sort(arr)
print(sorted_arr)


