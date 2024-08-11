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