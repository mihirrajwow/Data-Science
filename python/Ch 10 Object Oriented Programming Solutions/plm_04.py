class calculator:

    def __init__(self,num):
        self.number = num

    def Square(self):
        print(f"The square of {self.number} is {self.number **2}.")

    def Cube(self):
        print(f"The cube of {self.number} is {self.number **3}.")

    def SquareRoot(self):
        print(f"The square root of {self.number} is {self.number **(1/2)}.")

    @staticmethod
    def greet():
        print("****Hello there! welcome to the best calculator of the world.****")

ans = calculator(9)
ans.greet()
ans.Square()
ans.Cube()
ans.SquareRoot()