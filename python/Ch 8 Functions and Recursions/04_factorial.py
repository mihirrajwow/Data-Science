## n! = 1*2*3*4*...*(n)
## n! = (n-1)! * (n)

# n=4
# product = 1
# for i in range(n):
#     product = product * (i+1)
# print(product)

def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

# Recursion
def factorial_recursive(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial_recursive(n-1)

f = factorial_iter(6)
g = factorial_recursive(6)
print(f,g)