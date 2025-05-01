class Dnevnik:
    def __init__(self, imya, klass):
        self.imya = imya
        self.klass = klass
        self.predmety = {} #Словарь для хранения предметов и оценок. Ключ - наз пред, знач - список оценок

    def dobavit_predmet(self, predmet): #Добавляет предмет в дневник
        if predmet not in self.predmety:
            self.predmety[predmet] = []
            
    def postavit_ocenku(self, predmet, ocenka): #Ставит оценку по предмету
        if predmet in self.predmety:
            if isinstance(ocenka, int) and 1 <= ocenka <= 5:  #Проверка что оценка - целое число от 1 до 5
                self.predmety[predmet].append(ocenka)
    
    for i in range(0,7):            
        def posmotret_ocenki(self, predmet): #Выводит список оценок по предмету
            if predmet in self.predmety:
                print(f"Оценки по предмету '{predmet}': {self.predmety[predmet]}")
            else:
                print(f"Предмета '{predmet}' нет в дневнике.")

    def sredny_ball(self): #Рассчитывает и возвращает средний балл по всем предметам     
        vse_ocenki = []
        for predmet in self.predmety:
            vse_ocenki.extend(self.predmety[predmet])
        return sum(vse_ocenki) / len(vse_ocenki)

    def vyvesti_informaciu(self): #Выводит основную информацию о дневнике
        print(f"Дневник ученика:")
        print(f"  Имя: {self.imya}")
        print(f"  Класс: {self.klass}б")
        print(f"  Предметы: {(self.predmety)}") # Выводим список предметов

ivan_dnevnik = Dnevnik("Иван", 9) # Пример использования

ivan_dnevnik.dobavit_predmet("Математика") # Добавляем предметы
ivan_dnevnik.dobavit_predmet("Русский язык")
ivan_dnevnik.dobavit_predmet("История")

ivan_dnevnik.postavit_ocenku("Математика", 4) # Ставим оценки
ivan_dnevnik.postavit_ocenku("Математика", 5)
ivan_dnevnik.postavit_ocenku("Русский язык", 3)
ivan_dnevnik.postavit_ocenku("История", 5)

ivan_dnevnik.posmotret_ocenki("Математика") # Смотрим оценки по математике

ivan_dnevnik.vyvesti_informaciu() # Выводим информацию о дневнике

sredny_ball = ivan_dnevnik.sredny_ball() # Вычисляем средний балл
print(f"Средний балл: {sredny_ball}")
