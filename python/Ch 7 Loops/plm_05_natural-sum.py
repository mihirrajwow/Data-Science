n=int(input("Enter a number: "))
sum=0

## Sum of first n natural numbers using for loop
# for i in range(1,n+1):
#     sum+=i

## Sum of first n natural numbers using while loop
j=1
while j<n+1:
    sum+=j
    j+=1

print(f"The sum of first {n} natural numbers is {sum}.")