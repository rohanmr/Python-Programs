list=[1,2,3,5,4,6,7]

sum=0

for i in list:
    if i == 5:
        raise Exception("5 is not allowed")
    else:
        sum += i
    
    print(sum)

