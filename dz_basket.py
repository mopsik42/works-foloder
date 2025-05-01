import random

pl_1=input("Игрок 1 введите имя: ") #player_1
pl_2=input("Игрок 2 введите имя: ") #player_2

force_hit_1=0 #изначальная сила игрока 1
force_hit_2=0 
rnd_point=0 #генерируемое число
points_1=0
points_2=0
max_point=10

print("Сила игрока должна быть от 1 до 10")
print(f"Для победы необходимо набрать {max_point} очков")

while True:
    force_hit_1=int(input(f"{pl_1}: введите силу броска: "))
    force_hit_2=int(input(f"{pl_2}: введите силу броска: "))
    rnd_point=random.randint(1,10)
    print(f"случайное число: {rnd_point}")

    #Алгоритм подсчета кол-во очков для игрока 1 
    if abs(rnd_point-force_hit_1)==2:  
        points_1=points_1+1
        print(f"{pl_1}: получает +1 очко. Всего:{points_1}")
    if abs(rnd_point-force_hit_1)==1:
        points_1=points_1+2
        print(f"{pl_1}: получает +2 очка. Всего:{points_1}")
    if abs(rnd_point-force_hit_1)==0:
        points_1=points_1+3
        print(f"{pl_1}: получает +3 очка. Всего:{points_1}")
        
    #Алгоритм подсчета кол-во очков для игрока 2
    if abs(rnd_point-force_hit_2)==2:
        points_2=points_2+1
        print(f"{pl_2}: получает +1 очко. Всего:{points_2}")
    if abs(rnd_point-force_hit_2)==1:
        points_2=points_2+2
        print(f"{pl_2}: получает +2 очка. Всего:{points_2}")
    if abs(rnd_point-force_hit_2)==0:
        points_2=points_2+3
        print(f"{pl_2}: получает +3 очка. Всего:{points_2}")
    print(f"счет {points_1} : {points_2}")                                             
    with open('data.txt','a',encoding='utf-8') as f:
        f.write(f"счет: {points_1} : {points_2}"+'\n')  
    if points_1>=max_point or points_2>=max_point:
        break
    
# объявление победителя    
if points_1>points_2:
    print(f"{pl_1}: победил с счетом {points_1} : {points_2}")
    with open('data.txt','a',encoding='utf-8') as f:
        f.write(f"игрок 1 победил со счетом: {points_1}"+'\n')
elif points_2>points_1:
    print(f"{pl_2}: победил с счетом {points_2} : {points_1}")
    with open('data.txt','a',encoding='utf-8') as f:
        f.write(f"игрок 2 победил со счетом: {points_2}"+'\n')
else :    
    print(f"ничья с счетом {points_2} : {points_1}")


              