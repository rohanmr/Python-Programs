class queue:
    def __init__(self) -> None:
        self.values=[]
    
    def enqueue(self,x):
        self.values.append(x)

    def dequeue(self):
        front = self.values[0]
        self.values=self.values[1:] #deleting first element using slicing
        return front


q=queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)

print("Queue element is:",q.values)

print("Dequeue element is :",q.dequeue())

print("New queue list :",q.values)
