class Player:
  def __init__(self, inventory, health):
    self.inventory = inventory
    self.health = health

class Enemy:
  def __init__(self, health, attack_power):
    self.health = health
    self.attack_power = attack_power

class Room:
  def __init__(self, name, description, exits, items, enemies):
    self.name = name
    self.description = description
    self.exits = exits
    self.items = items
    self.enemies = enemies

class Item:
  def __init__(self, name, description):
    self.name = name
    self.description = description

def play_game():
  # Define player
  player = Player([], 100)

  # Define enemies
  goblin = Enemy(50, 10)
  dragon = Enemy(100, 20)

  # Define rooms
  bedroom = Room("Bedroom", "You are in a cozy bedroom.", ["north"], ["key"], [])
  kitchen = Room("Kitchen", "You are in a spacious kitchen.", ["east"], ["cake"], [goblin])
  living_room = Room("Living Room", "You are in a comfortable living room.", ["south"], ["book"], [])
  bathroom = Room("Bathroom", "You are in a clean bathroom.", ["west"], ["toothbrush"], [])
  treasure_room = Room("Treasure Room", "You are in a room filled with treasure.", [], ["gold", "diamond"], [dragon])

  # Initialize game variables
  game_over = False
  player_position = bedroom

  # Game loop
  while not game_over:
    # Print current room
    print(player_position.name)
    print(player_position.description)
    print("Available exits:", ", ".join(player_position.exits))
    print("Enemies in room:", ", ".join([enemy.name for enemy in player_position.enemies]))
    print("Inventory:", ", ".join(player.inventory))
    print("Health:", player.health)

    # Handle player's move
    move = input("Enter a command: ")

    if move.lower() == "q":
      game_over = True
    elif move.lower() == "go north":
      if "north" in player_position.exits:
        player_position = bedroom
      else:
        print("You can't go that way.")
    elif move.lower() == "go east":
      if "east" in player_position.exits:
        player_position = kitchen
      else:
        print("You can't go that way.")
    elif move.lower() == "go south":
      if "south" in player_position.exits:
        player_position = living_room
      else:
        print("You can't go that way.")
    elif move.lower() == "go west":
      if "west" in player_position.exits:
        player_position = bathroom
      else:
        print("You can't go that way.")
    elif move.lower().startswith("pick up"):
      item_to_pick_up = move[8:]
      if item_to_pick_up in player_position.items:
        player.inventory.append(item_to_pick_up)
        player_position.items.remove(item_to_pick_up)
        print("You picked up the", item_to_pick_up)
      else:
        print("You can't pick that up.")
    elif move.lower().startswith("drop"):
      item_to_drop = move[5:]
      if item_to_drop in player.inventory:
        player_position.items.append(item_to_drop)
        player.inventory.remove(item_to_drop)
        print("You dropped the", item_to_drop)
      else:
        print("You don't have that item.")
    elif move.lower() == "fight":
      if player_position.enemies:
        enemy = player_position.enemies[0]
        print("You are fighting a", enemy.name)
        while player.health > 0 and enemy.health > 0:
          player.health -= enemy.attack_power
          enemy.health -= player.attack_power
          print("Your health:", player.health)
          print(enemy.name, "health:", enemy.health)
        if player.health > 0:
          print("You defeated the", enemy.name)
          player_position.enemies.remove(enemy)
        else:
          print("You were defeated by the", enemy.name)
          game_over = True
      else:
        print("There are no enemies here.")
    elif move.lower() == "flee":
      if player_position.enemies:
        print("You fled from the", enemy.name)
        player_position = bedroom
      else:
        print("There are no enemies here.")
    else:
      print("I didn't understand that command.")

    # Check if player has won the game
    if player_position == treasure_room and not player_position.enemies:
      print("Congratulations, you won the game!")
      game_over = True

# Start the game
play_game()

# Define classes for different types of items
class Weapon:
  def __init__(self, name, damage):
    self.name = name
    self.damage = damage

class Armor:
  def __init__(self, name, defense):
    self.name = name
    self.defense = defense

class Potion:
  def __init__(self, name, health):
    self.name = name
    self.health = health

# Define classes for different types of enemies
class Skeleton:
  def __init__(self, health, attack_power):
    self.name = "Skeleton"
    self.health = health
    self.attack_power = attack_power

class Zombie:
  def __init__(self, health, attack_power):
    self.name = "Zombie"
    self.health = health
    self.attack_power = attack_power

class Boss:
  def __init__(self, health, attack_power):
    self.name = "Boss"
    self.health = health
    self.attack_power = attack_power

# Define classes for different types of rooms
class PuzzleRoom:
  def __init__(self, name, description, exits, items):
    self.name = name
    self.description = description
    self.exits = exits
    self.items = items
    self.puzzle = "Solve the puzzle to unlock the exit."

class TrapRoom:
  def __init__(self, name, description, exits, items, enemies):
    self.name = name
    self.description = description
    self.exits = exits
    self.items = items
    self.enemies = enemies
class BossRoom:
  def __init__(self, name, description, exits, enemies):
    self.name = name
    self.description = description
    self.exits = exits
    self.enemies = enemies

# Define a Player class to represent the player character
class Player:
  def __init__(self, inventory, health, attack_power, defense):
    self.inventory = inventory
    self.health = health
    self.attack_power = attack_power
    self.defense = defense

# Define a function to play the game
def play_game():
  # Define weapons
  sword = Weapon("Sword", 10)
  axe = Weapon("Axe", 20)

  # Define armor
  shield = Armor("Shield", 5)
  helmet = Armor("Helmet", 10)

  # Define potions
  health_potion = Potion("Health Potion", 20)
  mana_potion = Potion("Mana Potion", 10)

  # Define enemies
  skeleton1 = Skeleton(50, 10)
  skeleton2 = Skeleton(50, 10)
  zombie1 = Zombie(100, 20)
  zombie2 = Zombie(100, 20)
  boss = Boss(200, 30)

  # Define rooms
  bedroom = Room("Bedroom", "You are in a cozy bedroom.", ["north"], ["key"], [])
  kitchen = Room("Kitchen", "You are in a spacious kitchen.", ["east"], ["cake"], [skeleton1, skeleton2])
  living_room = Room("Living Room", "You are in a comfortable living room.", ["south"], ["book"], [])
  bathroom = Room("Bathroom", "You are in a clean bathroom.", ["west"], ["toothbrush"], [])
  puzzle_room = PuzzleRoom("Puzzle Room", "You are in a room with a puzzle.", [], [health_potion, mana_potion], "Solve the puzzle to unlock the exit.")
  trap_room = TrapRoom("Trap Room", "You are in a room with traps.", [], [shield, helmet], [zombie1, zombie2])
  boss_room = BossRoom("Boss Room", "You are in a room with the boss.", ["boss"], [boss])

  # Initialize game variables
  game_over = False
  player_position = bedroom

  # Define player
  player = Player([], 100, 10, 5)

  # Game loop
  while not game_over:
    # Print current room
    print(player_position.name)
    print(player_position.description)
    print("Available exits:", ", ".join(player_position.exits))
    print("Items in room:", ", ".join(player_position.items))
    print("Enemies in room:", ", ".join([enemy.name for enemy in player_position.enemies]))
    if isinstance(player_position, PuzzleRoom):
      print(player_position.puzzle)
    print("Inventory:", ", ".join([item.name for item in player.inventory]))
    print("Health:", player.health)




"""
As you can see it is repeating itself but this is REALLY DETAILED

"""