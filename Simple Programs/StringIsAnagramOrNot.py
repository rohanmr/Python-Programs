# Check if two strings are Anagram or not.

str1=input("Enter the word: ")
str2=input("Enter the another word: ")

if len(str1) == len(str2):
    str1_sorted=sorted(str1)
    str2_sorted=sorted(str2)

    if str1_sorted == str2_sorted:
        print("The string is Anagram")
    else:
        print("The String is not Anagram")
else:
    print("The String is not Anagram")