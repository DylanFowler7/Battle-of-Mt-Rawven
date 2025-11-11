class Units:
    wind_walker_number = 0
    tactician_number = 0
    drummer_number = 0
    paladin_number = 0
    investor_number = 0
    
    def __init__(self):
        self.name = ""
        self.health = 1
        self.attack = 1
        self.movement = 1
        self.ability = 0
        self.has_moved_this_turn = False
    
    def __str__(self):
        return f"{self.name} {self.number}(Current location{self.location})"
        
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
    def __init__(self):
        Units.__init__(self)
        self.name = "Wind_Walker"
        Units.wind_walker_number += 1
        self.number = Units.wind_walker_number
        self.location = ""
    
    def __repr__(self):
        return f"{self.name} {self.number}"   

class Tactician(Units):
    def __init__(self):
        Units.__init__(self)
        self.name = "Tactician"
        self.ability = 1
        Units.tactician_number += 1
        self.number = Units.tactician_number
        self.location = ""
    
    def __repr__(self):
        return f"{self.name} {self.number}"

class Drummer(Units):
    def __init__(self):
        Units.__init__(self)
        self.name = "Drummer"
        self.attack = 0
        Units.drummer_number += 1
        self.number = Units.drummer_number
        self.location = ""
        
    def __repr__(self):
        return f"{self.name} {self.number}"

class Paladin(Units):
    def __init__(self):
        Units.__init__(self)
        self.name = "Paladin"
        self.health = 2
        Units.paladin_number += 1
        self.number = Units.paladin_number
        self.location = ""
        
    def __repr__(self):
        return f"{self.name} {self.number}"

class Investor(Units):
    def __init__(self):
        Units.__init__(self)
        self.name = "Investor"
        Units.investor_number += 1
        self.number = Units.investor_number
        self.location = ""
        
    def __repr__(self):
        return f"{self.name} {self.number}"
        
