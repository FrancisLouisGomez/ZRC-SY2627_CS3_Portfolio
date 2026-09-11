class HERO:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def take_damage(self, amount):
        self.hp -= amount
        
Arthur = HERO("Arthur", 100)
Morgana = HERO("Morgana", 100)

Arthur.take_damage(10)
print(Arthur.hp)
print(Morgana.hp)