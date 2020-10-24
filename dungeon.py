import random as rand

# Player can get a loot after beat the monster

# Weapon class
class Weapon:
    attack: int
    level: int
    # Construct a weapon base on given level
    # randomly set its attack base on the given level
    def __init__(self, level):
        self.level = level
        self.attack = rand.randrange(level*10 + 1, (level+1)*10)

# Plate class
class Plate:
    armor: int
    level: int

    # Construct a plate base on given level
    # randomly set its armor base on the given level
    def __init__(self, level):
        self.level = level
        self.armor = rand.randrange(level*10 + 1, (level+1)*10)

# Player class
class Player:
    HP: int
    Weapon: Weapon
    Plate: Plate
    level: int

    # Construct a plate base on game difficulty(hp of the player), hard means less hp, easy means more hp
    # player can equip weapon and plate
    def __init__(self, hp):
        self.HP = hp
        self.level = 0
        self.Weapon = Weapon(0)
        self.Plate = Plate(0)

# Rock, Paper and Scissor class
class RPS:

    value: int
    label: str

    # Construct a RPS instance
    # 0 for Rock, 1 for Paper, 2 for Scissor
    def __init__(self, value):
        self.value = value
        if value == 0:
            self.label = "Rock"
        elif value == 1:
            self.label = "Paper"
        elif value == 2:
            self.label = "Scissor"

    # Compare function of two RPS object
    # return 1 if self wins, return 0 if draw, return -1 if self lose
    def compare(self, other):
        if self.value == other.value:
            return 0
        if self.value - other.value == 1:
            return 1
        if self.value - other.value == 2:
            return -1
        if self.value - other.value == -1:
            return -1
        if self.value - other.value == -2:
            return 1

# Dungeon class
class Dungeon:
    level = int
    Monster_HP: int
    attack: int
    Loots = []

    # Construct a new level of dungeon,
    # randomly set the dungeon's monster (has hp and attack), loot chest (has weapons and plates) base on the given level
    def __init__(self, level):
        self.level = level
        self.Monster_HP = rand.randrange(level * 10 + 1, (level+1) * 10)
        self.attack = rand.randrange(level * 10 + 1, (level+1) * 10)
        num_loots_weapons = rand.randrange(1, level+2)
        num_loots_plates = rand.randrange(1, level+2)

        for w in range(num_loots_weapons):
            self.Loots.append(Weapon(level+1))

        for p in range(num_loots_plates):
            self.Loots.append(Plate(level+1))
