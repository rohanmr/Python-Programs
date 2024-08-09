# Print your name 10 times without using loop and manually

count=1

def Printer(name):
    global count
    if count <=10:
        print(name)
        count+=1
        Printer(name)


Printer("Rohan Maindarkar")