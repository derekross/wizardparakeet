# exploration.py
from battle import battle
from wizard_parakeet import WizardParakeet
from enemy import Enemy
from zone import Zone

def explore_zone(player, zone):
    print(f"Entering {zone.name}...")

    for enemy in zone.enemies:
        battle(player, enemy)