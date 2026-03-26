class player():
    def __init__(self,name):
        self.name = name
        self.hp = 100
        self.attack = 10
        self.alive = True

    def attack(self):
        print(f"{self.name} swings their weapon dealing {self.attack} damage!")

    def take_damage(self):
        print(f"{self.name} is hit by the enemy!")
        self.hp -= 50

    def heal(self):
        print(f"{self.name} uses a health potion!")
        self.hp += 25

    def is_alive(self):
        if self.hp > 0:
            self.alive = False
