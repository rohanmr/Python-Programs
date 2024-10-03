arr=[12,55,6,1,2,77,44,66,20,10,78,4,3,99,5]

def margSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid=len(arr)//2

    l_half=arr[:mid]
    r_half=arr[mid:]

    l_half=margSort(l_half)
    r_half=margSort(r_half)

    return marge(l_half,r_half)


def marge(left,right):
    new=[]
    i,j=0,0

    while i < len(left) and j <len(right):
        if left[i]<right[j]:
            new.append(left[i])
            i+=1
        else:
            new.append(right[j])
            j+=1

    new.extend(left[i:])
    new.extend(right[j:])

    return new


sorted_arr=margSort(arr)
print(sorted_arr)