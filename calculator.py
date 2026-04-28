import math
class Calculator:
    """Performs arithmetic operations. Raises typed exceptions for invalid
inputs."""
    def add(self, a: float, b: float) -> float: 
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        return a * b
    
    def divide(self, a: float, b: float) -> float: 
        if b == 0:
            raise ZeroDivisionError
        else:
            return a / b
        
    def power(self, base: float, exp: float) -> float: 
        return math.pow(base, exp)
    
    def square_root(self, a: float) -> float:
        if a < 0:
            return ValueError
        else:
            return math.sqrt(a)

    def modulus(self, a: float, b: float) -> float: 
        if b == 0: 
            return ZeroDivisionError
        else:
            return a % b
        
    def floor_divide(self, a: float, b: float) -> float: 
        if b == 0:
            return ZeroDivisionError
        return math.floor(a / b)