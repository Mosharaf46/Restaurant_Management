from menu import Menu

class Restaurant:
    def __init__(self,name):
        self.name=name
        self.employees=[] #database of the employee
        self.menu=Menu()
        
        
    def add_employees(self,employee):
        self.employees.append(employee)
        
    def view_employees(self):
        print("----------------------Employee list----------------------")
        
        print(f"{'Name':<20}{'Email':<30}{'Phone':<15}{'Address':<25}")

        for emp in self.employees:
            print(f"{emp.name:<20}{emp.email:<30}{emp.phone:<15}{emp.address:<25}")

    print("\n")
