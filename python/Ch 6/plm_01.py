n1=int(input("Enter number 1: "))
n2=int(input("Enter number 2: "))
n3=int(input("Enter number 3: "))
n4=int(input("Enter number 4: "))

# List Method to find the greatest number
# n=[n1,n2,n3,n4]
# n.sort()
# print("The greatest number is ",n[3 ])

# If-elif-else statements method to find the greatest number
if(n1>n4):
    f1=n1
else:
    f1=n4
if(n2>n3):
    f2=n2
else:
    f2=n3
if(f2>f1):
    print(f2," is greatest")
else:
    print(f1," is greatest")