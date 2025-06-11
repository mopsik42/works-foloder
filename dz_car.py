class Person:
    def __init__(self,name):
        self.name=name
    
    def __str__(self):
        return self.name

class Car:
    def __init__(self, driver):
        self.driver = driver
        self.passengers=[] # список пассажиров который изначально пуст 
        self.trunk=[] # список вещей который изначально пуст 
        self.bagas_weight=0 # общий вес багажника
    
    def add_passenger(self,passenger):
        if len(self.passengers)>=4: # если уже 4 пасажира
            print("Нельзя посадить больше 4 пассажиров") #вывод ошибки 
            return
        self.passengers.append(passenger) # если все норм то добаляем пасажира 
    
    def add_in_bagas(self,item_name,item_weight):
        if self.bagas_weight+item_weight>50: # если багаж > 50 то выводим ошибку в строке ниже
            print("Превышен максимальный вес багажника (50кг)")
            return
        self.trunk.append((item_name, item_weight)) # добавляем вещь в багаж
        self.bagas_weight+=item_weight # увиличиваем вес
    
    def __str__(self):
        result=f"Машина с водителем {self.driver}\n" # информация о водителе 
        
        if not self.passengers: # если нет пасажиров
            result+="Пассажиры:нет\n"
        else: # если есть
            result+="Пассажиры:" + ",".join([str(p) for p in self.passengers])+"\n"
        
        result+=f"Багажник(вес: {self.bagas_weight}кг):\n" # инфа о багажнике
        if not self.trunk: # если нет вещей
            result+="пуст"
        else:  # если есть вещи
            for item in self.trunk: # эту и нежи строку я посмотрел в инете не сам ее сделал
                result+= f"{item[0]} ({item[1]}кг)\n" # добавляем каждую вещь
        
        return result

driver=Person("Иван")
car=Car(driver)

car.add_passenger(Person("Аня"))
car.add_passenger(Person("Петр"))
car.add_passenger(Person("Мария"))

car.add_in_bagas("Чемодан",15)
car.add_in_bagas("Рюкзак",5)
car.add_in_bagas("Коробка",10)

print(car)

car.add_passenger(Person("Дмитрий"))
car.add_passenger(Person("Ольга"))  

car.add_in_bagas("Гиря",30)  
