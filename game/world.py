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