class Employee:
    company = "Google"

    def __init__(self,name,salary,subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created!")

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")

    # def getSalary(self,sign):
    #     print(f"Salary for this employee working in {self.company} is {self.salary}\n{sign}")
    
    # @staticmethod
    # def greet():
    #     print("Good Morning, Sir")

    # @staticmethod
    # def time():
    #     print("The time is 5:05 am in the morning.")

mihir = Employee("Mihir",100,"YouTube")
# mihir = Employee() --> This throws an error(missing 3 required positional arguments)
mihir.getDetails()