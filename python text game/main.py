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
    print("Items in room:",
