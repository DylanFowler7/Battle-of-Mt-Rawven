class Units:
    
    def __init__(self):
        self.name = ""
        self.health = 1
        self.attack = 1
        self.movement = 1
        self.ability = 0
        self.has_moved_this_turn = False
    
    def __str__(self):
        return f"{self.name} {self.number}"
    
    def unit_display(self):
        return f"{self.name} {self.number}(Current location: {self.location})"
        
class Scout(Units):
    def __init__(self, number):
        Units.__init__(self)
        self.name = "Scout"
        self.ability = 2
        self.location = ""
        self.number = number
        
    def __repr__(self):
        return f"Scout(name='{self.name}', number={self.number})" 
        
class Wind_walker(Units):
    def __init__(self, number):
        Units.__init__(self)
        self.name = "Wind_Walker"
        self.number = number
        self.location = ""
    
    def __repr__(self):
        return f"{self.name} {self.number}"   

class Tactician(Units):
    def __init__(self, number):
        Units.__init__(self)
        self.name = "Tactician"
        self.ability = 1
        self.number = number
        self.location = ""
    
    def __repr__(self):
        return f"{self.name} {self.number}"

class Drummer(Units):
    def __init__(self, number):
        Units.__init__(self)
        self.name = "Drummer"
        self.attack = 0
        self.number = number
        self.location = ""
        
    def __repr__(self):
        return f"{self.name} {self.number}"

class Paladin(Units):
    def __init__(self, number):
        Units.__init__(self)
        self.name = "Paladin"
        self.health = 2
        self.number = number
        self.location = ""
        
    def __repr__(self):
        return f"{self.name} {self.number}"

class Investor(Units):
    def __init__(self, number):
        Units.__init__(self)
        self.name = "Investor"
        self.number = number
        self.location = ""
        
    def __repr__(self):
        return f"{self.name} {self.number}"
        
