class Character:
    """Representacion de los distintos personajes que puede controlar un jugador"""
    
    def __init__(self):
        pass
    
    def equipWeapon(self, weapon):
        self._weapon = weapon
        
    def equipArmor(self, armor):
        self._armor = armor
        
    def equipItem(self, item):
        self._item = item
        
    def control(self, town):
        town.attemptControl(self)
        
    def influence(self, location):
        location.attemptInfluence(self) 
                
    def extortion(self, location):
        location.attemptExtortion(self)
    
    def trade(self, town):
        town.attemptTrade(self)
    
class Leader(Character):
    """Personaje lider de cada jugador"""

class Thug(Character):
    """Personaje Maton"""

class Professional(Character):
    """Personaje Profesional"""
    
class Lawyer(Character):
    """Personaje Abogado"""
    
class Bussinessman(Character):
    """Personaje Comerciante"""
    
class Hacker(Character):
    """Personaje Hacker"""
        