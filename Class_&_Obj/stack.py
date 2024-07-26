class stack:
    def __init__(self) -> None:
        self.value=[]
    
    def Push(self,x):
        self.value=[x]+self.value
    
    def Pop(self):
        return self.value.pop(0)
    

s=stack()

s.Push(10)
s.Push(20)
s.Push(30)
s.Push(40)
s.Push(50)
s.Push(60)

print("Element list:",s.value)

print("Deleted element is :",s.Pop())

print("New Element list:",s.value)
