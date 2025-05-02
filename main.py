class Pupil:
    def __init__(self, name):
        self.name = name

class Dnevnik:
    def __init__(self):
        self.__owner = ""
        self.monthData={}

    @property
    def owner(self):
        return self.owner
    
    @owner.setter
    def owner(self, newOwner):
        self.__owner  = newOwner
    
    def add(self,subject:str, value:int):
        if subject in self.monthData:
            print(f'{subject} есть в списке.')
        else: self.monthData[subject] = value
    
    def __str__(self):
        return "OK"


chel = Pupil("Dima")
dnevnik = Dnevnik()
dnevnik.owner = chel.name
dnevnik.add("История",0)
dnevnik.add("Химия",3)
dnevnik.add("Биология",3)
print(dnevnik)