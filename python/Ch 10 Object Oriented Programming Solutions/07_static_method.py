class Employee:
    company = "Google"

    def getSalary(self,sign):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{sign}")
    
    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 5:05 am in the morning.")

mihir = Employee()
mihir.salary = 100000
# mihir.getSalary() # Employee.getSalary(mihir)
mihir.getSalary("Thanks!") # Employee.getSalary(mihir)

mihir.greet() # Employee.greet()

julie = Employee()
julie.time()