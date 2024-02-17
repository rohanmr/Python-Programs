
class employee:
    def putdata(self):
        self.id=int(input("Enter Employee Id:"))
        self.name=input("Enter Employee Name: ")
        self.salery=float(input("Enter Employee Salery:"))

    def display(self):
        print("|---------------------------------|")
        print("Employee Id is:",self.id)
        print("Employee Name is:",self.name)
        print("Employee Salery is:",self.salery)
        print("|----------------------------------|")

a=employee()
a.putdata()
a.display()