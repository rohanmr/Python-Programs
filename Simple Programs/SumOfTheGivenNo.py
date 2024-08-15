# Sum of the Digit of a No (Ex – 123 = 1+2+3 = 6)

n=int(input("Enter the no: "))

result=0

while n > 0:
    result+= n % 10
    n=n // 10

print(result)

# result=0

# while n > 0:
#     digit= n % 10

#     result=result+digit

#     n=n//10

# print("your sum is:",result)

