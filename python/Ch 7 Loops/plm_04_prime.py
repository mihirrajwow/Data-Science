num=int(input("Enter a number: "))

# prime=False
# for i in range(2,num):
#     if num%i!=0:
#         prime=True
#     else:
#         break

prime=True
for i in range(2,num):
    if(num%i==0):
        prime=False
        break

if prime:
    print(f"The given number {num} is prime.")
else:
    print(f"The given number {num} is NOT a prime.")