class Number:
    def __init__(self,num):
        self.num = num

    def __add__(self,other):
        print("Lets add")
        return self.num + other.num
    
    def __mul__(self,other):
        print("Lets multiply")
        return self.num * other.num
    
n1=Number(4)
n2=Number(6)
sm=n1+n2
ml=n1*n2
print(sm,ml)