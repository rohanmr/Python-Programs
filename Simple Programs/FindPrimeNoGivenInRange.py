# Find Prime No in a given ranges ( ex prime no b/w 1 to 20 : 2,3,5,7,11,13,17,19)

num=int(input("Enter the number: "))

for i in range(2, num+1):
    for j in range(2,i):
        if(i % j) == 0:
            break
    else:
        print(i)

