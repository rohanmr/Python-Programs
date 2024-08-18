
string=input("Enter the string or number:")

print("Your Entered no is:",string)

revStr=string[::-1]

if revStr == string:
    print("The string or number is Palindrome")
else:
    print("The string or number is not Palindrome")
    