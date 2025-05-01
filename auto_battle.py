import random
from termcolor import colored as clr

from items import Weapon
from items import Potion


class Player: # Класс человека 
    def __init__(self,name:str,health:int,weapon:'Weapon'=Weapon("Рука",5)):
        self.name=name
        self.health=health
        self.weapon= weapon
        self.potion=None 

    def attack(self,target:'Player'): # Функция в которой игрок наносит урон другому игроку 
        target.health-=self.weapon.damage
        dmg_str = clr(f"- {str(self.weapon.damage)}",'red')
        print(f'🔥{self.name} наносит урон {target.name} с {self.weapon.name} и сносит {dmg_str} ХП!🔥')

    def use_potion(self): # Функция в которой игрок использует зелье здоровья (если оно есть) и повышает свое здоровье
        if self.potion:
          self.health+=self.potion.effect
          if self.potion.effect>0:
            print(f"{self.name} использует {self.potion} {self.potion.description} Повышает здоровье на:{self.potion.effect}")
          else:
            print(f"{self.name} использует {self.potion} {self.potion.description} Уменьшает здоровье на:{self.potion.effect}")      
          self.potion=None 
        else:
          print("нет зелья")

    def is_dead(self)->bool: # Функция где мы определяем когда игрок умрет
        return self.health<=0

    def __str__(self): # Функция которая выводит: имя игрока, здоровье 
        return f'💥 Игрок:{self.name} (здоровье: {self.health}) (оружие: {self.weapon})💥'

def print_step():
    print("-"*40)
    print(f'🟢 Игрок_1:{player_1.name} (здоровье: {player_1.health}) 🟢 Игрок_2: {player_2.name} (здоровье: {player_2.health})')
    print("-"*40)

player_1 = Player(clr('pastyx','yellow'), random.randint(50, 250),Weapon("Sword", 20))
player_2 = Player(clr('frikadelka','cyan'), random.randint(50, 250), Weapon("Axe", 15))

print_step()

round_num=1 

while not (player_1.is_dead() or player_2.is_dead()): # Цикл где игроки дерутся, используют зелья(при необходимости) 
  print(f"ROUND:{round_num}")

  if random.random()<1: 
    player_1.potion=Potion() 
    print(f"{player_1.name} активирует {player_1.potion}")

  if player_1.potion:
      player_1.use_potion()
  else:
      player_1.attack(player_2) 

  print(player_1) 
  print(player_2)

  if player_2.is_dead(): 
        break

  if random.random()<0.3: 
    player_2.potion=Potion() 
    print(f"{player_2.name} активирует {player_2.potion}")

  if player_2.potion:
      player_2.use_potion()
  else:
      player_2.attack(player_1) 

  print(player_1) 
  print(player_2)

  print_step()
  round_num+=1 

if not player_1.is_dead():        # Определение кто победил 
    print(f'👑{player_1.name} победил!👑')
elif not player_2.is_dead():
    print(f'👑{player_2.name} победил!👑')
else:
    print("ничья")