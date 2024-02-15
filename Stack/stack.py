class stack:
    def __init__(self) -> None:
        self.values=[]
    
    def push(self,x):
        self.values=[x]+self.values

    def pop(self):
        self.values.pop(0)

s=stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

print(s.values)