x=int(input("Enter the first no:"))
y=int(input("Enter the second no:"))

def FindHcf(x,y):
    if x > y :
        smaller = y
    else:
        smaller = x

        for i in range(1,smaller+1):
            if((x % i == 0) and (y % i == 0)):
                hcf = i

        return hcf


result=FindHcf(x,y)
print(result)