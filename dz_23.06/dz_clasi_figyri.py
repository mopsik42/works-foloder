class Kvadrat:
    def __init__(self, a):
        self.a = a
        
    def __str__(self):
        return f'Площадь квадрата : {self.a * self.a}'
            
class Treygol:
    def __init__(self, a, h):
        self.a = a
        self.h = h
    def __str__(self):
        return f'Площадь треугольника : {self.a * self.h /2}'            
        
class  Pramoygol: 
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return f'Площадь треугольника : {self.a * self.b}' 

kvadrat = Kvadrat(2)
treygol = Treygol(2,4)
pramoygol = Pramoygol(2,5)  

print(kvadrat)
print(treygol)
print(pramoygol)
         


    
        
        
        