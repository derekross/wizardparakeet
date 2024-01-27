# battle.py
import random
from wizard_parakeet import WizardParakeet
from enemy import Enemy

def battle(player, enemy):
    print(f"A wild {enemy.name} appears!")

    while player.health > 0 and enemy.health > 0:
        print("\nOptions:")
        print("1. Millet Blast")
        print("2. Wing Slash")
        print("3. Decoy Summon")
        print("4. Lightning Zap")
        print("5. Teleport")
        print("6. Nature's Blessing")
        print("7. Tail Whip")
        print("8. Eat Millet")

        if player.name == "Wand Upgrader":
            print("9. Upgrade Wand")

        choice = input("Enter your choice: ")

        if choice == "1":
            player_damage = player.millet_blast()
            enemy_damage = enemy.attack()

            print(f"{player.name} casts Millet Blast and deals {player_damage} damage to the {enemy.name}!")
            print(f"The {enemy.name} retaliates and deals {enemy_damage} damage to {player.name}!")

            player.take_damage(enemy_damage)
            enemy.health -= player_damage

        elif choice == "2":
            player_damage = player.wing_slash()
            enemy_damage = enemy.attack()

            print(f"{player.name} performs Wing Slash and deals {player_damage} damage to the {enemy.name}!")
            print(f"The {enemy.name} retaliates and deals {enemy_damage} damage to {player.name}!")

            player.take_damage(enemy_damage)
            enemy.health -= player_damage

        elif choice == "3":
            if player.decoy_summon():
                print("The decoy parakeet successfully distracts the enemy!")

        elif choice == "4":
            player_damage = player.lightning_zap()
            print(f"{player.name} casts Lightning Zap, dealing {player_damage} damage to the {enemy.name}!")
            enemy.health -= player_damage

        elif choice == "5":
            result = player.teleport()
            if result == "escape":
                print(f"{player.name} successfully escapes from battle!")
                return

        elif choice == "6":
            success = player.nature_blessing()
            if success:
                print(f"{player.name} is blessed by nature, restoring health and mana!")

        elif choice == "7":
            if player.tail_whip():
                print(f"{player.name} executes a Tail Whip, stunning the {enemy.name}!")

        elif choice == "8":
            player.eat_millet()

        elif choice == "9" and player.name == "Wand Upgrader":
            success = player.upgrade_wand()
            if success:
                print(f"{player.name} successfully upgrades the wand!")

        else:
            print("Invalid choice. Try again.")

        print(f"{player.name}'s Health: {player.health}")
        print(f"{enemy.name}'s Health: {enemy.health}")

    if player.health <= 0:
        print(f"{player.name} is defeated. Game Over.")
    else:
        millet_reward = enemy.get_millet_reward()
        player.millets += millet_reward

        if enemy.drop_wand():
            player.get_stronger_wand()

        if enemy.drop_power_stone():
            player.collect_power_stone()

        print(f"{player.name} defeats the {enemy.name}! {millet_reward} millet(s) obtained!")