class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

mihir = Employee()
mihir.salary = 100000
mihir.getSalary() # Employee.getSalary(mihir)
