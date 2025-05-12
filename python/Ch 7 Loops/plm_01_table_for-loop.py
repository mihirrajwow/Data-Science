a=int(input("Enter a number: "))
print("The table of",a,"is given below: ")
# for i in range(a,(a*10)+1,a):
#     print(i)
for j in range(1,11):
    # print(str(a)+" x "+str(j)+" = "+str(a*j))
    print(f"{a} x {j} = {a*j}")