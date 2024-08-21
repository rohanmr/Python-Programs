list=[10,50,40,60,90,800,30]


maximum=list[0]
minimum=list[0]

for i in range(len(list)):
    if list[i]>maximum:
        maximum=list[i]
    elif list[i]<minimum:
        minimum=list[i]

    
print("Maximum is",maximum)

print("Minimum is ",minimum)



# num=[10,50,40,60,90,800,30]


# maximum=num[0]
# minimum=num[0]

# for i in range(len(num)):
#     if num[i]>maximum:
#         maximum=num[i]
#     elif num[i]<minimum:
#         minimum=num[i]

    
# print("Maximum is",maximum)

# print("Minimum is ",minimum)