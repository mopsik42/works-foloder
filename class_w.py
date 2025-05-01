class Food:
    def __init__(self,food_name="milk",poison=0):
        self.food_name = food_name
        self.poison = poison
    
    def get_name(self):
        return self.food_name
    
    def get_poison(self):
        return self.poison
        
        
    
class Person:
    def __init__(self,name="Chucha",age=12,grow=100):
        namesplit = name.split(" ")
        self.fname = namesplit[1]
        self.lname =namesplit[0]
        self.age = age
        self.grow = grow
    
    def print(self):
        print(f'name = {self.fname} lastname = {self.lname} age = {self.age} grow = {self.grow}')
    
    def run(self):
        print(f'{self.name} побежал')
        
    def stop(self):
        print(f'{self.name} остановился')    
    
    def changeName(self,newName):
        self.name = newName
    
    def eatFood(self,food):
        if food.get_poison()==1:
            print(f'{self.fname} не будет есть {food.get_name()}')
        else:
            print(f'{self.fname} ест {food.get_name()}')
            
    
ivan = Person("Иванов Иван",15,165)

tyhlyak= Food("Тухляк",1)

ivan.eatFood(tyhlyak)