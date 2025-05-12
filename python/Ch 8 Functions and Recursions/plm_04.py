# n! = (n-1)! * n
# sum(n) = sum(n-1) + n

def sum_recur(n):
    if n==0:
        return 0
    else:
        return n + sum_recur(n-1)

print(sum_recur(10))