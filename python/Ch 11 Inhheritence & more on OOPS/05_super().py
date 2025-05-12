class Person:
    country = "India"

    def __init__(self):
        print("Initializing Person...")

    def takeBreath(self):
        print("I am breathing.")

class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__()
        print("Initializing Employee...")

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath()
        print("I am luckily breathing.(employee)")

class Programmer(Employee):
    company = "Fiverr"

    def __init__(self):
        super().__init__()
        print("Initializing Programmer...")

    def getSalary(self):
        print("No salary to programmers")

    def takeBreath(self):
        super().takeBreath()
        print("I am luckily breathing.(programemr)")

# p=Person()
# p.takeBreath()

# e=Employee()
# e.takeBreath()

pr=Programmer()
# pr.takeBreath()
