# Питомец
class Pet:
    def __init__(self, name):
        self.name=name  # имя питомца

# Жилец
class Person:
    def __init__(self, name):
        self.name=name  # имя жильца
        self.pet=[]  # питомец 

# Квартира
class Flat:
    def __init__(self, number):
        self.number=number    # номер квартиры
        self.residents=[]    # жильцы в квартире

# Дом
class House:
    def __init__(self):
        self.flats=[] # Создаю 3 подъезда в каждом 2 этажа на каждом 2 квартиры
        for entrance in [1, 2, 3]:
            for floor in [1, 2]:
                for flat in [1, 2]:
                    self.flats.append(Flat(f"{entrance}-{floor}-{flat}")) # Номер квартиры подъезд этаж квартира
    
    def find_flat(self, number): # Найти квартиру по номеру
        for flat in self.flats:
            if flat.number==number:
                return flat
        return []

house=House()  # Создаем дом

flat=house.find_flat("1-1-1")
if flat:
    resident=Person("Иван")
    resident.pet=Pet("Барсик")
    flat.residents.append(resident)

flat=house.find_flat("2-2-2")
if flat:
    resident=Person("Мария")
    flat.residents.append(resident)

print("1. Все квартиры в доме:")
for flat in house.flats:
    print(f"Квартира {flat.number}: {len(flat.residents)} жильцов")

print("\n2. Квартира 1-1-1:")
flat = house.find_flat("1-1-1")
if flat:
    for resident in flat.residents:
        print(f"Жилец: {resident.name}")
        if resident.pet:
            print(f"Питомец: {resident.pet.name}")

print("\n3. Квартиры на 2 этаже 1 подъезда:")
for flat in house.flats:
    if flat.number.startswith("1-2-"):
        print(f"Квартира {flat.number}")
                                     