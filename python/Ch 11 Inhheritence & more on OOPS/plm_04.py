# (a+bi)(c+di) = (ac-bd) + (ad+bc)i

class complex:

    def __init__(self,r,i):
        self.real=r
        self.imaginary=i

    def __add__(self,c):
        return complex(self.real + c.real, self.imaginary + c.imaginary)
    
    def __mul__(self,c):
        self.mulReal = (self.real * c.real) - (self.imaginary * c.imaginary)
        self.mulImag = (self.real * c.imaginary) + (self.imaginary * c.real)
        return complex(self.mulReal, self.mulImag)
    
    def __str__(self):
        if self.imaginary < 0:
            return f"{self.real} + {- self.imaginary}i"
        elif self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"

c1=complex(3,2)
c2=complex(1,7)
print(c1*c2)
print(c1+c2)
