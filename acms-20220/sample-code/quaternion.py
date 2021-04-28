import math

class Quaternion:
    
    # The constructor expects the four coefficients, passed as an iterable.
    def __init__(self, *args):        
        args = list(args)
        
        L = len(args)
        
        if L > 4:
            raise ValueError("Too many arguments (maximum 4)")
           
        if L == 0:
            args = [0.0, 0.0, 0.0, 0.0]
        elif L == 1:
            if isinstance(args[0], Quaternion):
                args = [args[0].__w, args[0].__x, args[0].__y, args[0].__z]
            elif isinstance(args[0], complex):
                args = [args[0].real, args[0].imag, 0.0, 0.0]
            else:
                args = [float(args[0]), 0.0, 0.0, 0.0]
        
        while len(args) < 4:
            args.append(0.0)
        
        # Prefacing an attribute with one or two underscores indicates
        # that the variable is not intended to be public.
        # If two leading underscores are used, the variable name will be 
        # "mangled" so that it cannot be accessed directly from outside the
        # class (although it is still possible to access with workarounds).
        
        self.__w = float(args[0])
        self.__x = float(args[1])
        self.__y = float(args[2])
        self.__z = float(args[3])
        
    # The __repr__ function is intended to return a string representation
    # of the object. The representation should be such that evaluating it
    # will allow the object to be reconstructed.
    def __repr__(self):
        return "Quaternion(" + ", ".join(str(elem) for elem in \
                        [self.__w, self.__x, self.__y, self.__z]) + ")"
            
            
    # __str__ returns a "pretty" string representation of a Quaternion.
    def __str__(self):
        data = (self.__w, self.__x, self.__y, self.__z)
        rep = str(data[0])
        for elem, unit in zip(data[1:], ["i", "j", "k"]):
            if elem < 0:
                rep += " - "
            else:
                rep += " + "
            rep += str(abs(elem)) + unit
        return rep
    
                
    # Used to implement hashing. The definition below is reasonably common.
    # Two objects which hash equal should compare equal with ==.
    def __hash__(self):
        return hash(repr(self))
    
    
    # Used to implement obtaining values with []. Here we have implemented
    # __getitem__ but not __setitem__ to discourage users from changing an
    # existing Quaternion object directly.
    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("Index must be int")
        elif index < 0 or index >= 4:
            raise IndexError("Index must be int from 0 to 3 inclusive")
        
        return {0 : self.__w, 1 : self.__x, 2 : self.__y, 3 : self.__z}[index]
                
        
    # Equality operator
    def __eq__(self, rhs):
        rhs = Quaternion(rhs)
        
        return self.__w == rhs.__w and self.__x == rhs.__x \
                and self.__y == rhs.__y and self.__z == rhs.__z
                
    # Less than operator. This is NOT typically defined mathematically for
    # quaternions, but can be useful in programming contexts. The order here
    # is lexicographical.
    def __lt__(self, rhs):
        rhs = Quaternion(rhs)
        return (self.__w, self.__x, self.__y, self.__z) < \
               (rhs.__w, rhs.__x, rhs.__y, rhs.__z)
    
    
    # Less than or equal to operator. See above for less than operator.
    def __le__(self, rhs):
        return self < rhs or self == rhs
    
    
    # Unary minus
    def __neg__(self):
        return Quaternion(-self.__w, -self.__x, -self.__y, -self.__z)
    
    
    # Unary plus
    def __pos__(self):
        return self
   
    
    # Addition operator
    def __add__(self, rhs):
        rhs = Quaternion(rhs)
        return Quaternion(self.__w + rhs.__w, self.__x + rhs.__x,
                          self.__y + rhs.__y, self.__z + rhs.__z)
  
    
    # Subtraction operator
    def __sub__(self, rhs):
        rhs = Quaternion(rhs)
        return Quaternion(self.__w - rhs.__w, self.__x - rhs.__x,
                          self.__y - rhs.__y, self.__z - rhs.__z)
    
    
    # Multiplication operator
    def __mul__(self, rhs):
        rhs = Quaternion(rhs)
        # Complicated formula for the product of two quaternions!
        return Quaternion(self.__w * rhs.__w - self.__x * rhs.__x - \
                          self.__y * rhs.__y - self.__z * rhs.__z,
                          self.__w * rhs.__x + self.__x * rhs.__w + \
                          self.__y * rhs.__z - self.__z * rhs.__y,
                          self.__w * rhs.__y - self.__x * rhs.__z + \
                          self.__y * rhs.__w + self.__z * rhs.__x,
                          self.__w * rhs.__z + self.__x * rhs.__y - \
                          self.__y * rhs.__x + self.__z * rhs.__w)
            
            
    # Division operator    
    def __truediv__(self, rhs):
        rhs = Quaternion(rhs)
        return self * rhs.inv()
            
    
    # Right division operator. Called when the rhs of + is a Quaternion 
    # but the left hand side is not.
    def __radd__(self, lhs):
        lhs = Quaternion(lhs)
        return self + lhs
    
    
    # Right subtraction operator.
    def __rsub__(self, lhs):
        lhs = Quaternion(lhs)
        return lhs - self
        
    
    # Right multiplication operator.
    def __rmul__(self, lhs):
        lhs = Quaternion(lhs)
        return lhs * self


    # Right division operator.
    def __rtruediv__(self, lhs):
        lhs = Quaternion(lhs)
        return lhs * self.inv()

    
    # Inversion operator. Used to compute the multiplicative inverse of 
    # a Quaternion.    
    def inv(self):
        norm_sq = self.__w ** 2 + self.__x ** 2 + self.__y ** 2 + self.__z ** 2 
        if norm_sq == 0.0:
            raise ZeroDivisionError("Cannot invert zero Quaternion")
        else:
            return Quaternion(self.__w/norm_sq, -self.__x/norm_sq,
                              -self.__y/norm_sq, -self.__z/norm_sq)
    
    
    # Conjugation operator
    def conj(self):
        return Quaternion(self.__w, -self.__x, -self.__y, -self.__z)
    
    
    # Magic method for to call abs on a Quaternion
    def __abs__(self):
        return math.hypot(self.__w, self.__x, self.__y, self.__z)
    
    
    # Compute the norm of a Quaternion. Same as abs, except called
    # differently.
    def norm(self):
        return abs(self)
        
    
    # Allows a Quaternion to be used in a Boolean context.
    def __bool__(self):
        return abs(self) != 0.0
    
    
    # Recursive implementation of pow
    def __pow__(self, e):
        if not isinstance(e, int):
            raise TypeError("Exponent to pow or ** must be an int")
        
        if e == 0:
            return Quaternion(1.0)
        
        if e < 0:
            base = self.inv()
            e = -e
        else:
            base = self
            
        if e % 2 == 0:
            val = base ** (e//2)
            return val * val
        else:
            val = base ** (e//2)
            return base * val * val
       
        
# Determine if two Quaternions are close to one another in absolute value.
# This is useful due to rounding error in floating point arithmetic.
# Note that this function has been defined outside the class definition
# and is not a method of the class.
def close(lhs, rhs, tolerance = 10**-12):
    lhs = Quaternion(lhs)
    rhs = Quaternion(rhs)
    return max(abs(lhs[i] - rhs[i]) for i in range(4)) < tolerance