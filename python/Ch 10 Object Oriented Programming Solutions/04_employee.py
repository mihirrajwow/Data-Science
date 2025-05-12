class Employee:
    company = "Google" 
    salary = 100

mihir = Employee()
riya = Employee()

mihir.salary = 400
riya.salary = 300

print(mihir.company)
print(riya.company)
Employee.company = "YouTube"
print(mihir.company)
print(riya.company)

print(mihir.salary)
print(riya.salary)