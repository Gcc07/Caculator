import math
class Calculator:
    """Performs arithmetic operations. Raises typed exceptions for invalid
inputs."""
    def add(self, a: float, b: float) -> float: 
        '''Adds two numbers together and returns the sum.'''
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        '''Subtracts one number from another and returns the difference.'''
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        '''Multiplies two numbers and returns their product.'''
        return a * b
    
    def divide(self, a: float, b: float) -> float: 
        '''Divides one number by another and returns the quotient.'''
        if b == 0:
            raise ZeroDivisionError
        else:
            return a / b
        
    def power(self, base: float, exp: float) -> float: 
        '''Repeatedly multiplies a base number by n (exp) number of times.'''
        return math.pow(base, exp)
    
    def square_root(self, a: float) -> float:
        '''Returns a value that, multiplied by itself, equals the inputted number.'''
        if a < 0:
            return ValueError
        else:
            return math.sqrt(a)

    def modulus(self, a: float, b: float) -> float: 
        '''Divides one number by another, returning the remainder of the operation'''
        if b == 0: 
            return ZeroDivisionError
        else:
            return a % b
        
    def floor_divide(self, a: float, b: float) -> float: 
        '''Divides one number by another, returning a floored (rounded down) quotient.'''
        if b == 0:
            return ZeroDivisionError
        return math.floor(a / b)