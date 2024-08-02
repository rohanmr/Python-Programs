# Print duplicate present in the list
list=[10,20,20,40,60,50,40,30,70,30]
n=len(list)
d=[]

for i in range(n):
    for j in range(i+1,n):
        if list[i]==list[j] and list[i] not in d:
            d.append(list[i])
print(d)





# Using Builtin Method
# for i in list:
#     if list.count(i)>1 and i not in d:
#         d.append(i)

# print(d)