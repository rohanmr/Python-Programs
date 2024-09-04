# Find out  all the duplicates in the input string.

string=input("Enter the string: ")

def findDuplicate(string):
    d=[]

    for i in set(string):
        if string.count(i)>1:
            d.append(i)
    
    return d


res=findDuplicate(string)

print(res)