# You are give a string you have make this type of output 
# Input is : "a3b5c6d4"
# Output is:"aaabbbbbccccccdddd"


string="a3b2c5d4"
outputStr=""

for char in string:
    if char.isalpha():
        result=char
    else:
        num=int(char)
        outputStr=outputStr+(num*result)

print(outputStr)