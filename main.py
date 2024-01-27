# main.py
from wizard_parakeet import WizardParakeet
from enemy import Enemy
from zone import Zone
from exploration import explore_zone

def main():
    player_name = input("Enter your parakeet's name: ")
    player = WizardParakeet(player_name)

    derek = WizardParakeet("Derek")  # Added Derek to the game

    print(f"Welcome, {player.name} and {derek.name} the Wizard Parakeets!")

    zones = [
        Zone("Forest", [Enemy("Evil Cat", 30, (5, 15), (1, 3), 5, 10)], "Magic Berries"),
        Zone("Cave", [Enemy("Goblin", 40, (8, 18), (1, 3), 10, 5)], "Gemstone"),
        Zone("Mountains", [Enemy("Dragon", 60, (15, 25), (2, 4), 15, 15)], "Dragon Scale"),
        Zone("Cloud Castle", [Enemy("Air Elemental", 50, (10, 20), (3, 5), 20, 20)], "Cloud Feather"),
        Zone("Volcano", [Enemy("Fire Elemental", 55, (12, 22), (3, 6), 15, 25)], "Volcanic Rock"),
        Zone("Underwater Cavern", [Enemy("Squid Guardian", 45, (10, 18), (2, 5), 10, 30)], "Pearl"),
        Zone("Enchanted Garden", [Enemy("Charming Butterfly", 35, (8, 15), (1, 4), 5, 15)], "Enchanted Flower"),
        Zone("Boss Room", [Enemy("Angrt Macaw", 750, (30, 60), (4, 8), 25, 10)], "Frozen Crystal"),
        Zone("Wand Enhancement Chamber", [], "Wand Upgrade"),
    ]

    while player.health > 0 and derek.health > 0:
        print("\nOptions:")
        print("1. Explore a Zone")
        print("2. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Available Zones:")
            for i, zone in enumerate(zones, start=1):
                print(f"{i}. {zone.name}")

            zone_choice = int(input("Enter the number of the zone you want to explore: ")) - 1

            if 0 <= zone_choice < len(zones):
                if zones[zone_choice].name == "Wand Enhancement Chamber":
                    success = player.upgrade_wand()
                    if success:
                        print(f"{player.name} successfully upgrades the wand!")
                else:
                    explore_zone(player, zones[zone_choice])

                # Derek explores the same zone
                explore_zone(derek, zones[zone_choice])

            else:
                print("Invalid zone choice. Try again.")

        elif choice == "2":
            print(f"{player.name} and {derek.name} decide to give up on the quest for millet. Game Over.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
