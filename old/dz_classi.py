import random
class Animal:    # Класс животных(имя,состояние,звук)
    def __init__(self,name,state,voice):
        self.name=name
        self.state=state 
        self.voice=voice 
               
class Person:    #Класс человаека где определится что будет если он дотронется до кокого либо животного 
    def __init__(self, name, health=100):
        self.name=name
        self.health=health
    def touch(self, animal):
        print(f"Человек трогает {animal.name}")
        
        if animal.state=="aggressive": # Что будет если состояние животного агресивное
            self.health-=5
            print(f"{animal.name} кусает {self.name} {animal.voice} теперь у {self.name} {self.health} здоровья")
            
        elif animal.state=="friendly": # Что будет если состояние животного дружелюбное
            self.health+=5
            print(f"{animal.name} ластится {animal.voice} теперь у {self.name} {self.health} здоровья")
                              
cat=Animal("мурка", "friendly","Мяу")
dog=Animal("шарик", "aggressive","Гав")
cow=Animal("коровка", "friendly","Муу")
person=Person(name="Николай")
print(cat)
person.touch(cat)
person.touch(dog)
person.touch(cow)
