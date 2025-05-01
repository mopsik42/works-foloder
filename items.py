import random
from termcolor import colored as clr



class Weapon: # Класс оружия
    def __init__(self,name:str,damage:int):
        self.name=name
        self.damage=damage

    def __str__(self): # Какое оружие и какой у него урон 
        return f"{clr(self.name,'blue')}(урон:{self.damage})"
    
# ---------------------------------------------------------------------------------
class Potion: # Класс зелье 
    def __init__(self):
        self.skill=random.choice(['poison','heal'])
        if self.skill=='poison':
            self.effect=-random.randint(10,30)  
            self.description="Яд:Наносит урон!"
        else:
            self.effect=random.randint(10, 30)   
            self.description="Исцеление:Восстанавливает здоровье"
            
    def __str__(self): # Название зелье и какой у него эфект 
        return f"Зелье:{self.description}(Эффект:{self.effect})"
