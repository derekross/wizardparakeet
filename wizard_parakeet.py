# wizard_parakeet.py
import random

class WizardParakeet:
    def __init__(self, name):
        self.name = name
        self.health = 150
        self.mana = 50
        self.millets = 5
        self.wand_damage = 10
        self.wand_level = 1
        self.power_stones = 0  # New attribute for storing power stones

    def millet_blast(self):
        cost = random.randint(5, 10) - self.wand_level
        if self.mana >= cost:
            damage = random.randint(15 + self.wand_damage, 25 + self.wand_damage)
            self.mana -= cost
            return damage
        else:
            print("Not enough mana to cast Millet Blast!")
            return 0

    def wing_slash(self):
        cost = random.randint(8, 15) - self.wand_level
        if self.mana >= cost:
            damage = random.randint(10 + self.wand_damage, 20 + self.wand_damage)
            self.mana -= cost
            return damage
        else:
            print("Not enough mana to perform Wing Slash!")
            return 0

    def decoy_summon(self):
        cost = random.randint(12, 20) - self.wand_level
        if self.mana >= cost:
            print(f"{self.name} summons a decoy to distract the enemy!")
            self.mana -= cost
            return True
        else:
            print("Not enough mana to summon a decoy!")
            return False

    def lightning_zap(self):
        cost = random.randint(18, 25) - self.wand_level
        if self.mana >= cost:
            print(f"{self.name} casts Lightning Zap, dealing massive damage to the enemy!")
            self.mana -= cost
            return random.randint(25 + self.wand_damage, 35 + self.wand_damage)
        else:
            print("Not enough mana to cast Lightning Zap!")
            return 0

    def teleport(self):
        cost = random.randint(20, 30) - self.wand_level
        if self.mana >= cost:
            print(f"{self.name} uses Teleport to escape from battle!")
            self.mana -= cost
            return "escape"
        else:
            print("Not enough mana to cast Teleport!")
            return 0

    def nature_blessing(self):
        cost = random.randint(25, 35) - self.wand_level
        if self.mana >= cost:
            print(f"{self.name} invokes Nature's Blessing, restoring health and mana!")
            self.mana -= cost
            self.health += random.randint(20, 30)
            self.mana += random.randint(15, 25)  # Regenerate mana
            return True
        else:
            print("Not enough mana to cast Nature's Blessing!")
            return False

    def tail_whip(self):
        cost = random.randint(15, 20) - self.wand_level
        if self.mana >= cost:
            print(f"{self.name} executes a powerful Tail Whip, stunning the enemy!")
            self.mana -= cost
            return True
        else:
            print("Not enough mana to perform Tail Whip!")
            return False

    def upgrade_wand(self):
        cost = random.randint(30, 40)
        if self.mana >= cost:
            print(f"{self.name} enters the Wand Enhancement Chamber and upgrades the wand!")
            self.mana -= cost
            self.wand_damage += random.randint(5, 15)
            self.wand_level += 1
            print(f"{self.name}'s wand damage is now {self.wand_damage}!")
            print(f"{self.name}'s wand level is now {self.wand_level}!")
            return True
        else:
            print("Not enough mana to upgrade the wand!")
            return False

    def take_damage(self, damage):
        self.health -= damage

    def eat_millet(self):
        if self.millets > 0:
            print(f"{self.name} munches on the delicious millet and regains 20 health!")
            self.health += 20
            self.mana += random.randint(10, 15)  # Regenerate mana
            self.millets -= 1
        else:
            print("No millets left! Defeat enemies to earn more.")

    def get_stronger_wand(self):
        print(f"Congratulations! {self.name} found a stronger wand!")
        self.wand_damage += random.randint(5, 20)
        self.wand_level += 1
        print(f"{self.name}'s wand damage is now {self.wand_damage}!")
        print(f"{self.name}'s wand level is now {self.wand_level}!")

    def collect_power_stone(self):
        print(f"{self.name} found a Power Stone!")
        self.power_stones += 1
