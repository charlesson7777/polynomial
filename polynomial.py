class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

class Int:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)
    
class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
    def __repr__(self):
        if(self.p2==0):
            return repr(self.p1) + " cannot be divided by 0"
        else: 
            return repr(self.p1) + " / " + repr(self.p2)
            
class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2)
    

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, Add):#This line verifies if self.p1 is an object of the Add class
            if isinstance(self.p2, Add):#This line verifies if self.p2 is an object of the Add class
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)


poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)

print(Add(3,6))
print(Div(4,0))
print(Sub(5,8))
print(Mul(3,6))
