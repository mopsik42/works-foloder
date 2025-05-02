class Pupil:
    def __init__(self, name):
        self.name = name

class Dnevnik:
    def __init__(self):
        self.owner = ""
        self.monthData={}

    @property
    def owner(self):
        return self.owner
    
    @owner.setter
    def owner(self, newOwner):
        self.owner  = newOwner