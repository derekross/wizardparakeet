# enemy.py
import random

class Enemy:
    def __init__(self, name, health, damage_range, millet_reward_range, wand_drop_rate, power_stone_drop_rate):
        self.name = name
        self.health = health
        self.damage_range = damage_range
        self.millet_reward_range = millet_reward_range
        self.wand_drop_rate = wand_drop_rate
        self.power_stone_drop_rate = power_stone_drop_rate

    def attack(self):
        damage = random.randint(*self.damage_range)
        return damage

    def get_millet_reward(self):
        return random.randint(*self.millet_reward_range)

    def drop_wand(self):
        return random.randint(1, 20) <= self.wand_drop_rate

    def drop_power_stone(self):
        return random.randint(1, 100) <= self.power_stone_drop_rate