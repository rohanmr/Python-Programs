#  From list of items move zero to last of the list

list=[1,0,2,0,4,0,0,5,8,9,3,7,6]

for i in list:
    if i == 0:
        list.remove(i)
        list.append(i)

print("New List: ",list)