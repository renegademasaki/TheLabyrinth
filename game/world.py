from .puzzles import Puzzle
from .items import Container, Item
from .npcs import create_goblin

class Room:
  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.exits = {}
    self.items = []
    self.puzzle = None
    self.locked_exits = {}
    self.locked_items = {}
    self.npc = None

  def add_exit(self, direction, room, requires_puzzle=None):
    """Add an exit to the room, optionally requiring a puzzle to be solved"""
    if requires_puzzle:
      self.locked_exits[direction] = (room, requires_puzzle)
    else:
      self.exits[direction] = room

  def add_item(self, item):
    """Add an item to the room"""
    self.items.append(item)

  def remove_item(self, item_name):
    """Remove an item from the room by name"""
    for item in self.items:
      if item.name.lower() == item_name.lower():
        self.items.remove(item)
        return item
    return None

  def get_item(self, item_name):
    """Get an item from the room by name without removing it"""
    for item in self.items:
      if item.name.lower() == item_name.lower():
        return item
    return None

  def add_puzzle(self, puzzle):
    """Add a puzzle to the room"""
    self.puzzle = puzzle

  def add_npc(self, npc):
    """Add an NPC to the room"""
    self.npc = npc

  def unlock_exit(self, direction):
    """Unlock an exit if it was locked by a puzzle"""
    if direction in self.locked_exits:
      room, _ = self.locked_exits[direction]
      self.exits[direction] = room
      del self.locked_exits[direction]

class World:
  def __init__(self):
    self.rooms = {}
    self.starting_room = None
    #why is there an extra _ here?
    self._create_world()

  def _create_world(self):
    """Create the game world with rooms, connections, and puzzles"""
    # Create rooms
    entrance = Room(
      "Castle Entrance",
      "You stand before a massive stone castle. The ancient walls loom above you."
    )

    great_hall = Room(
      "Great Hall",
      "A vast hall with high ceilings. Dusty tapestries hang on the walls."
    )

    courtyard = Room(
      "Courtyard",
      "An open courtyard with a dried-up fountain in the center."
    )

    library = Room(
      "Library",
      "A vast library filled with dusty tomes and ancient books."
    )

    treasure_room = Room(
      "Treasure Room",
      "A magnificent room filled with glittering treasures and artifacts."
    )

    # Create and add goblin to courtyard
    goblin = create_goblin()
    courtyard.add_npc(goblin)

    # Create puzzles
    door_puzzle = Puzzle(
      "Locked Door",
      "A locked door stands before you. An empty slot protrudes from the wall next to it.",
      "lever",
      "You pull the lever and the door unlocks!",
      ["lever"]
    )

    # Add puzzles to rooms
    great_hall.add_puzzle(door_puzzle)

    # Create locked chest with contents
    lever = Item(
      "Lever",
      "An old wooden lever with a rusted handle.",
      puzzle_hint="This looks like it might fit in a slot."
    )

    locked_chest = Container(
      "Locked Chest",
      "A wooden chest with a rusted lock.",
      required_key="Rusty Key",
      contents=[lever],
      can_take=False,
      puzzle_hint="The keyhole looks rusty, perhaps an old key would work?"
    )

    # Add items to rooms
    silver_coin = Item(
      "Silver Coin",
      "A shiny silver coin with a cracked zinc inlay.",
      puzzle_hint="Someone might find this valuable."
    )
    rusty_key = Item(
      "Rusty Key",
      "An old rusty key. It flakes and crumbles in your hand.",
      puzzle_hint="This might fit in a lock."
    )
    helm_of_knowledge = Item(
      "Helm of Knowledge",
      "A mysterious golden helm with a strange symbol on its front.",
      puzzle_hint="This might be useful for escaping the labyrinth."
    )
    
    great_hall.add_item(silver_coin)
    treasure_room.add_item(helm_of_knowledge)
    library.add_item(locked_chest)
    courtyard.add_item(rusty_key) # ***TEST CODE, goblin giving key to player not working***
    
    # Create connections between rooms
    entrance.add_exit("north", great_hall)
    great_hall.add_exit("south", entrance)
    great_hall.add_exit("west", courtyard)
    great_hall.add_exit("east", library)
    courtyard.add_exit("east", great_hall)
    library.add_exit("west", great_hall)
    # Add locked exit to treasure room
    great_hall.add_exit("north", treasure_room, door_puzzle)
    treasure_room.add_exit("south", great_hall)

    # Store rooms and set starting point
    self.rooms = {
      "entrance": entrance,
      "great_hall": great_hall,
      "courtyard": courtyard,
      "library": library,
      "treasure_room": treasure_room
    }
    self.starting_room = entrance

  def get_room_by_name(self, room_name):
    """Get a room by its name"""
    for room in self.rooms.values():
      if room.name.lower() == room_name.lower():
        return room
    return None