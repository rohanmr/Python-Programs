# Find the first non-repeating character in a string.

string=input("Enter the the string: ")

def first_non_repeating_char(string):
    
    for i in range(len(string)):
        if string.count(string[i])==1:
            return string[i]
            
    
    return None
    
    
res=first_non_repeating_char(string)
print(res)