class Calculator:
    def add(self, x, y):
        return x + y
    
    def substract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def Divide(self, x, y):
        return x / y
    
    def factorial(self, n):
        if (n == 0):
            return 1
        else:
            return self.factorial(n - 1) * n
        

    
