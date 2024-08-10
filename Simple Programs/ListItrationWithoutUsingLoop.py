# iterate on list without using loop

lst=eval(input("Enter the list: "))
start=eval(input("Enter the start index: "))
end=eval(input("Enter the end index:"))

def iteration(lst,start,end):
    if start<0 or start>=end or end >=len(lst):
        return
    
    print(lst[start])
    iteration(lst,start+1,end)


iteration(lst,start,end)