#sort dictionary using dict comprehension

dict1={4:"apple",1:"banana",6:"mango",5:"greps",2:"kiwi"}

d=sorted(dict1)
dict2={}

for i in d:
    dict2[i]=dict1[i]

print(dict2)