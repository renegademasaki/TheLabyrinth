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

    # Create connections between rooms
    entrance.add_exit("north", great_hall)
    great_hall.add_exit("south", entrance)
    great_hall.add_exit("west", courtyard)
    great_hall.add_exit("east", library)
    courtyard.add_exit("east", great_hall)
    library.add_exit("west", great_hall)
    # Add locked exit to treasure room
    #library.add_exit("north", treasure_room, door_puzzle)
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