from enum import Enum



class Team(Enum):
    bummy = 1
    suri = 2
    
    def __str__(self):
        return self.name

class Object(Enum):
    Background = 1
    Body = 2
    Clothing = 3
    Face = 4
    Hand = 5
    Hat = 6
    HeadAccessories = 7
    
    def __str__(self):
        return self.name
