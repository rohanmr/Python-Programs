# Print all pairs with given sum

list=[8,7,6,5,3,4,2,1,12,15]

n=len(list)

num=input("Enter the no to obtain the pair of sum: ")

for i in range(n):
    for j in range(i+1,n):
        if list[i]+list[j]==int(num):
            print(list[i],list[j])
        
