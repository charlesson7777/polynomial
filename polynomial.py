class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"
    
    def evaluate(self, x):
        return x
    
class Int:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)
    
    def evaluate(self, x):
        return self.i

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)
    
    def evaluate(self, x):
        return self.p1.evaluate(x) + self.p2.evaluate(x)
    
class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
    def __repr__(self):
        if isinstance(self.p1, (Add, Mul, Sub)):#This line verifies if self.p1 is an object of the Add class
            if isinstance(self.p2, (Add, Mul, Sub)):#This line verifies if self.p2 is an object of the Add class
                 return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) / " + repr(self.p2)
        if isinstance(self.p2, (Add, Mul, Sub)):
            return repr(self.p1) + " / ( " + repr(self.p2) + " )"
        if isinstance(self.p2, Int) and self.p2.i == 0:
            return "Can't divide by 0"
        return repr(self.p1) + " / ( " + repr(self.p2) + " )"
        
    
    def evaluate(self, x):
        if self.p2.evaluate(x) == 0:
            return "cannot divide by zero"
        return self.p1.evaluate(x) / self.p2.evaluate(x)
            
class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2)
    
    def evaluate(self, x):
        return self.p1.evaluate(x) - self.p2.evaluate(x)
    

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, (Add, Sub, Div)):#This line verifies if self.p1 is an object of the Add class
            if isinstance(self.p2, (Add, Sub,Div)):#This line verifies if self.p2 is an object of the Add class
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, (Add, Sub, Div)):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)
    
    def evaluate(self, x):
        return self.p1.evaluate(x) / self.p2.evaluate(x)


poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)

div_poly = Div(poly, Add(Int(2), X()))
sub_poly = Sub(poly, Mul(Int(3), X()))

print(div_poly)
print(sub_poly)

print(poly.evaluate(2))
