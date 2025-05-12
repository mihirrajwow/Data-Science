class Number:
    def __init__(self,num):
        self.num = num

    def __add__(self,other):
        print("Lets add")
        return self.num + other.num
    
    def __mul__(self,other):
        print("Lets multiply")
        return self.num * other.num
    
    def __str__(self):
        return f"Decimal Number: {self.num}"
    
    def __len__(self):
        return 1
    
n=Number(9)
print(n)
print(len(n))