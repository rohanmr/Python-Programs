
class employee:
    def PutData(self):
        self.id=int(input("Enter Employee Id:"))
        self.name=input("Enter Employee Name: ")
        self.salary=float(input("Enter Employee Salary:"))

    def display(self):
        print("|---------------------------------|")
        print("Employee Id is:",self.id)
        print("Employee Name is:",self.name)
        print("Employee Salary is:",self.salary)
        print("|----------------------------------|")

a=employee()
a.PutData()
a.display()