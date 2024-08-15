# Check if a given Number is Prime no or not ?

num=int(input("Enter the  Number: "))

if num > 1 :
    for i in range(2,num):
        if num % i == 0:
            print("No is not Prime no")
            break
        else:
            print("No is Prime no")
            break