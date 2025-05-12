class Employee:
    company = "Bharat Gas"
    salary = 5600
    salaryBonus = 400
    # salaryTotal = 6100

    @property
    def salaryTotal(self):
        return self.salary + self.salaryBonus

    @salaryTotal.setter
    def salaryTotal(self,val):
        self.salaryBonus = val - self.salary
    
e=Employee()
print(e.salaryTotal)
e.salaryTotal = 5800
print(e.salary)
print(e.salaryBonus)