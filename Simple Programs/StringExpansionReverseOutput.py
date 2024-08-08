# You are give a string you have make this type of output 
# Input is : "aaabbbbbccccccdddd" 
# Output is:"a3b5c6d4"

string="aaabbbbbccccccdddd" 

outputStr=""

char=string[0]
count=0

for ch in string:
    if ch == char:
        count+=1
    else:
        outputStr=outputStr+str(count)+char
        count=1
        char=ch 

outputStr=outputStr+str(count)+char

print(outputStr)