class stack:
    def __init__(self) -> None:
        self.values=[]
    
    def Push(self,x):
        self.values=[x]+self.values
    
    def Pop(self):
        return self.values.pop(0)


s=stack()

s.Push(10)
s.Push(20)
s.Push(30)
s.Push(40)
s.Push(50)

print("Elements in the stack:",s.values)

print("Deleted element is:",s.Pop())

print("New stack list is:", s.values)



