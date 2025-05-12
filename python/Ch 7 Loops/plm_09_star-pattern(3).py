n=int(input("Enter a digit: "))
print("*" * n)
for i in range(n-2):
    print("*", end="")
    print(" " * (n-2), end="")
    print("*")
    i+=1
print("*" * n)