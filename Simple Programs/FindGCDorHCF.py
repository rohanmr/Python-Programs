x=int(input("Enter the first no:"))
y=int(input("Enter the second no:"))

def FindHCF(x,y):
    if x > y:
        b = y
    else:
        b = x
    
    for i in range(1,b+1):
        if (x % i ==0) and (y % i == 0):
            hcf=i
        
    return hcf


res=FindHCF(x,y)
print("The HCF/GCD of the given nos is:",res)