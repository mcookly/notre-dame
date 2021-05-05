#!/usr/bin/env python3

import collections.abc

# Replace the "pass" statements with an actual implementation of each
# method/function so that the class behaves as expected. See the hw62main.py
# file for examples of the output that each of the methods should produce.
# I recommend building the class in steps:
# first, get __init__, __repr__ and __str__ to work as expected.
# After that, get degree, __pos__ and __neg__ to work as expected.
# Then, try for __add__, __radd__, etc., testing as you go.


class Polynomial:
    
    # initialize a polynomial using data of one of the following forms:
    # 1) another Polynomial
    # 2) a Sequence object (such as a list or tuple)
    # 3) a single float or int
    
    # Store the data for the class as an instance attribute named __coefs
    # which should store a tuple of floats. The zero polynomial should
    # be represented by the empty tuple. The coefficients should be stored
    # so that index i of the coefficients corresponds to the coefficient
    # of x^i in the polynomial. The last entry in the tuple should be
    # maintained as a non-zero value. Note that this may require trimming
    # the entries of the data passed in if data is a Sequence object.
    def __init__(self, data):
        coefs = list()
        if isinstance(data, Polynomial):
            coefs = data.__coefs
        elif isinstance(data, collections.abc.Sequence):
            tgl_add = False
            for cf in reversed(data):
                # Append first coef that is non-zero in reversed order.
                if tgl_add:
                    coefs.append(float(cf))
                elif cf != 0:
                    coefs.append(float(cf))
                    tgl_add = True # Add all values past non-zero coef.
            coefs = reversed(coefs)
        elif isinstance(data, (float, int)):
            coefs = float(data) if data else tuple()
        else:
            raise ValueError("Polynomial() can only accept int, float, \
            Sequence object, or another Polynomial")
        self.__coefs = tuple(coefs)
  
    # Return a representation that could be used to reconstruct the object.
    def __repr__(self):
        return "Polynomal((" + ", ".join([str(c) for c in self.__coefs]) + "))"
    
    # Return a "pretty" string representation of the object.
    def __str__(self):
        cfs = self.__coefs
        rep = str()
        # If polynomial is a zero polynomial
        if len(cfs) == 0:
            return "0.0"
        for i in reversed( range(len(cfs)) ):
            cfs_i = cfs[i]
            rep_sub = str() # substring for each x^i

            # Sign Pass
            if i != len(cfs)-1:
                if cfs_i > 0:
                    rep_sub += " + "
                elif cfs_i < 0:
                    rep_sub += " - "
            else:
                if cfs_i < 0:
                    rep_sub += "-"

            # Coefficient & Variable Pass
            if i != 0 and cfs_i != 0:
                # if not on last coefficient (constant)
                if abs(cfs_i) > 1:
                    # x needs a coefficient present
                    rep_sub += str(abs(cfs_i))
                rep_sub += f"x^{i}" if i != 1 else "x"
            elif cfs_i != 0:
                rep_sub += str(abs(cfs_i))
            rep += rep_sub
        return rep
    
    # hash function, no need to modify.
    def __hash__(self):
        return hash(repr(self))
    
    # Check for equality. Note that other may be a Polynomial or 
    # an int or float.    
    def __eq__(self, other):
        return self.__coefs == other.__coefs
    
    # Unary plus operator.
    def __pos__(self):
        return self
    
    # Unary minus operator
    def __neg__(self):
        new_coefs = [-c for c in self.__coefs]
        return Polynomial(new_coefs)
    
    # Polynomial addition. Note that rhs may be either a Polynomial or an
    # int or float.
    def __add__(self, rhs):
        scf = self.__coefs
        side_self = True # T: self, F: rhs
        # Check to see which polynomial is longer
        if isinstance(rhs, Polynomial):
            rcf = rhs.__coefs
            if len(scf) > len(rcf):
                iter_len = len(scf)
            else:
                iter_len = len(rcf)
                side_self = False # add rhs contents to end of new_coef
            new_coefs = list()
            for i in range(iter_len):
                try:
                    new_coefs.append(scf[i] + rcf[i])
                except IndexError:
                    if side_self:
                        new_coefs.extend(scf[i:])
                    else:
                        new_coefs.extend(rcf[i:])
                    break
        else:
            new_coefs = list(scf)
            new_coefs[0] += rhs
        return Polynomial(new_coefs)

    # Right addition operator. Note that lhs may be either a Polynomial or 
    # an int or float.
    def __radd__(self, lhs):
        scf = self.__coefs
        side_self = True # T: self, F: lhs

        # check to see which polynomial is longer
        if isinstance(lhs, Polynomial):
            lcf = lhs.__coefs
            if len(scf) > len(lcf):
                iter_len = len(scf)
            else:
                iter_len = len(lcf)
                side_self = False # add rhs contents to end of new_coef

            new_coefs = list()
            for i in range(iter_len):
                try:
                    new_coefs.append(scf[i] + lcf[i])
                except IndexError:
                    if side_self:
                        new_coefs.extend(scf[i:])
                    else:
                        new_coefs.extend(lcf[i:])
                    break
        else:
            new_coefs = list(scf)
            new_coefs[0] += lhs

        return Polynomial(new_coefs)
    
    # Subtraction operator. Note that rhs may be either a Polynomial or an
    # int or float.
    def __sub__(self, rhs):
        # NOTE. Uses __add__ method
        if isinstance(rhs, Polynomial):
            return self + -rhs
        else:
            new_coefs = list(self.__coefs)
            new_coefs[0] -= rhs
            return Polynomial(new_coefs)
    
    # Right subtraction operator. Note that lhs may be either a Polynomial or 
    # an int or float.
    def __rsub__(self, lhs):
        # NOTE. Uses __radd__ method
        if isinstance(lhs, Polynomial):
            return lhs + -self
        else:
            new_coefs = list(self.__coefs)
            new_coefs[0] -= lhs # intentionally flipped for return statement
            return -Polynomial(new_coefs)
    
    # Multiplication operator. Note that rhs may be either a Polynomial or
    # an int or float.
    def __mul__(self, rhs):
        # self: P1, rhs: P2
        cfs = self.__coefs
        if isinstance(rhs, Polynomial):
            r_cfs = rhs.__coefs  
            new_coefs = [0]*(self.degree()+rhs.degree()+1)
            # will ensure that highest degree of P1*P2 has an index
            for i in range(len(cfs)):
                # iterate through coefs in P1
                c1 = cfs[i]
                for j in range(len(r_cfs)):
                    # iterate through coefs in P2
                    c2 = r_cfs[j]
                    new_coef = c1*c2
                    new_coefs[i+j] += new_coef
        else:
            new_coefs = [c * rhs for c in self.__coefs] if rhs != 0 else 0
        return Polynomial(new_coefs)
    
    # Right multiplication operator. Note that lhs may be either a Polynomial
    # or an int or float.
    def __rmul__(self, lhs):
        # self: P2, lhs: P1
        cfs = self.__coefs
        if isinstance(lhs, Polynomial):
            l_cfs = lhs.__coefs
            new_coefs = [0]*(self.degree()+lhs.degree())
            # will ensure that highest degree of P1*P2 has an index
            for i in range(len(l_cfs)):
                # iterate through coefs in P1
                c1 = l_cfs[i]
                for j in range(len(cfs)):
                    # iterate through coefs in P2
                    c2 = cfs[j]
                    new_coef = c1*c2
                    new_coefs[i+j] += new_coef
        else:
            new_coefs = [lhs*c for c in self.__coefs] if lhs != 0 else 0
        return Polynomial(new_coefs)
        
    # Subscript operator []. index should be a non-negative integer. This
    # should support obtaining the coefficient of x^i in the polynomial,
    # even if i exceeds the degree of the polynomial (the coefficient is zero
    # in that case).
    def __getitem__(self, index):
        cfs = self.__coefs
        try:
            return cfs[index]
        except IndexError:
            if index >= 0:
                return 0.0
            else:
                raise IndexError("Please enter a non-negative index.")
    
    # Returns the degree of the polynomial. Note that the degree of the zero
    # polynomial is -inf by convention. (You could use -float("inf") or 
    # -math.inf for this value.)
    def degree(self):
        cfs = self.__coefs
        return len(cfs)-1 if len(cfs) != 0 else -float("inf")
    
    # Returns False for the zero polynomial, and True otherwise.
    def __bool__(self):
        return bool(self.__coefs)
    
    # pow function (for ** and pow). The exponent should be a non-negative
    # integer. Note that any polynomial to the zeroth power should return
    # a degree zero monic polynomial.
    def __pow__(self, e):
        new_poly = self
        if e == 0:
            # zero monic polynomial
            new_poly = Polynomial( [1.0] )
        else:
            for _ in range(e-1):
                new_poly *= self

        return new_poly
    
    # return the derivative of a polynomial.
    def prime(self):
        cfs = list(self.__coefs)
        new_coefs = [0]*len(cfs)
        for i in range(1, len(cfs)):
            new_cf = cfs[i] * i
            new_coefs[i-1] += new_cf
        return Polynomial(new_coefs)
    
# return a monic (leading coefficient 1) monomial of the specified 
# (non-negative) degree. Note that this function is not a method of the 
# Polynomial class, although it should return a Polynomial object.
def monomial(degree):
    coefs = [0]*(degree+1)
    coefs[-1] = 1.0
    return Polynomial(coefs)