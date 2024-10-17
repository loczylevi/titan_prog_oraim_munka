


import random

class Warrior:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.healt = int(health)
        self.attack_power = int(attack_power)
        self.vedekezes = random.randint(0,500)
        
    def Random_faktor(self):
        self.veletlen = random.randint(1,25)
        self.alakito = str(self.veletlen)
        self.osszead = "0." + self.alakito
        self.szazalek = float(self.osszead)
        self.random_faktor = self.attack_power * self.szazalek
        self.random_sebzes = self.random_faktor + self.attack_power
        return self.random_sebzes
    
    def enemy(self, e_health, e_attack_power):
        self.e_health = int(e_health)
        self.e_attack_power = int(e_attack_power)
        self.e_vedekezes = random.randint(0,500)
        
        
    def attack(self): #Ez a metódus csökkenti az ellenfél életerejét a támadási erővel.
        if self.name != "enemy":
            return self.e_healt - self.random_sebzes
        else:
            return self.healt - self.random_sebzes
        
    def is_alive(self): #Ez a metódus visszatér True értékkel, ha a harcos életereje nagyobb mint 0, és False-al, ha nem.
        if self.healt > 0:
            return True
        else:
            return False
        
        

ember = Warrior("pityu", 200, 400)

print(ember.enemy(12,65))


