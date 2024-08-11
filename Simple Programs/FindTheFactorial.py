num=int(input("enter the no: "))

def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num-1)

if num < 0:
    print("Factorial of negative no can not be calculated") 
elif num == 0:
    print("The factorial od 0  is 1")
else:
    result=fact(num)
    print(f"The factorial of {num} is {result}")
    





