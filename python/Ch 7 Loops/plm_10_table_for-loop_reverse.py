a=int(input("Enter a number: "))
print("The table of",a," in reverse order is given below: ")

for j in range(10,0,-1):
    print(f"{a} x {j} = {a*j}")