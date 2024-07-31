list=[20,30,50,40,70,90,60,100]

maximum=list[0]
minimum=list[0]

for i in range(len(list)):
    if list[i]>maximum:
        maximum=list[i]
    elif list[i]<minimum:
        minimum=list[i]

    
print("Maximum is",maximum)

print("Minimum is ",minimum)