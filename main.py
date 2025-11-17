import random

# You can add/remove cards here
CLASH_ROYALE_CARDS = [
    # Common
    "Archers", "Arrows", "Bomber", "Cannon", "Fire Spirits", "Goblin Gang",
    "Goblins", "Ice Spirit", "Knight", "Minions", "Rascals",
    "Royal Giant", "Royal Recruits", "Skeletons", "Spear Goblins",
    "Tesla", "Zap", "Barbarians", "Bats", "Bomb Tower",

    # Rare
    "Battle Healer", "Dart Goblin", "Earthquake", "Elixir Collector",
    "Fireball", "Flying Machine", "Furnace", "Goblin Cage", "Goblin Hut",
    "Heal Spirit", "Hog Rider", "Ice Golem", "Mini P.E.K.K.A", "Musketeer",
    "Phoenix", "Rocket", "Tombstone", "Valkyrie", "Wall Breakers",
    "Wizard", "Zappies", "Battle Ram", "Mega Minion",

    # Epic
    "Baby Dragon", "Balloon", "Barbarian Barrel", "Bowler", "Clone",
    "Dark Prince", "Electro Dragon", "Executioner", "Freeze",
    "Giant Skeleton", "Giant Snowball", "Goblin Barrel", "Goblin Drill",
    "Golem", "Guards", "Hunter", "Lightning", "Mirror", "P.E.K.K.A",
    "Poison", "Prince", "Rage", "Skeleton Army", "Skeleton Dragons",
    "Tornado", "Witch", "X-Bow",

    # Legendary
    "Bandit", "Electro Wizard", "Fisherman", "Graveyard",
    "Ice Wizard", "Inferno Dragon", "Lava Hound",
    "Log", "Lumberjack", "Magic Archer", "Mega Knight", "Miner",
    "Mother Witch", "Night Witch", "Princess", "Ram Rider",
    "Royal Ghost", "Sparky",

    # Champions
    "Archer Queen", "Golden Knight", "Skeleton King", "Monk", "Grand Warden",

    # Evolutions
    "Evolved Barbarians", "Evolved Firecracker", "Evolved Goblins",
    "Evolved Knight", "Evolved Royal Giant", "Evolved Skeletons",
    "Evolved Ice Spirit", "Evolved Archers", "Evolved Minion Horde",
    "Evolved Mortar", "Evolved Cannon Cart", "Evolved Musketeer",
    "Evolved Valkyrie"
]



def get_num_players():
    while True:
        try:
            n = int(input("How many players are playing? "))
            if n < 2:
                print("You need at least 2 players. Try again.")
            else:
                return n
        except ValueError:
            print("Please enter a valid integer.")


def get_player_names(num_players):
    names = []
    print("\nEnter player names:")
    for i in range(num_players):
        name = input(f"  Player {i + 1} name: ").strip()
        if not name:
            name = f"Player {i + 1}"
        names.append(name)
    return names


def assign_roles(names):
    num_players = len(names)
    imposter_index = random.randrange(num_players)

    # Choose ONE card for all crewmates
    shared_card = random.choice(CLASH_ROYALE_CARDS)

    roles = []
    for i, name in enumerate(names):
        if i == imposter_index:
            roles.append({"name": name, "role": "Imposter", "card": None})
        else:
            roles.append({"name": name, "role": "Crewmate", "card": shared_card})
    return roles


def reveal_roles_privately(roles):
    print("\nNow we will reveal roles one by one.")
    print("Make sure only the current player is looking at the screen!")
    input("\nPress Enter to start...")

    for info in roles:
        name = info["name"]
        input(f"\nPass the device to {name}. When they're ready, press Enter...")

        print("\n" + "=" * 40)
        print(f"{name}, this is your secret info:")
        if info["role"] == "Imposter":
            print("\n  👉 You are the IMPOSTER!")
            print("  You do NOT have a Clash Royale card.\n")
        else:
            print("\n  👉 You are a NOT THE IMPOSTER.")
            print(f"  Your Clash Royale card is: {info['card']}\n")
        print("=" * 40)

        input("\nPress Enter when you're done, then pass the device to the next player...")
        # Try to "clear" the screen a bit
        print("\n" * 50)


def main():
    print("=== Clash Royale Imposter Game ===")
    num_players = get_num_players()
    names = get_player_names(num_players)
    roles = assign_roles(names)
    reveal_roles_privately(roles)
    print("All roles have been revealed. Time to play and find the Imposter!")


if __name__ == "__main__":
    main()
