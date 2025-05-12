class Employee:
    company = "Google" 
    salary = 100

mihir = Employee()
riya = Employee()

# Creating instance attribute salary for both the objects
# mihir.salary = 400
# riya.salary = 300
riya.salary = 150
print(mihir.salary)
print(riya.salary)

# Below line throws an error as address is not present in instance/class 
# print(riya.address)