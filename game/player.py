class Player:
  def __init__(self, starting_room):
    self.current_room = starting_room
    self.inventory = []

  def move(self, direction):
    """Attempt to move the player in the specified direction.
    Returns True if the move was successful, False otherwise."""
    if direction in self.current_room.exits:
      self.current_room = self.current_room.exits[direction]
      return True
    return False

  def add_to_inventory(self, item):
    """Add an item to the player's inventory."""
    self.inventory.append(item)

  def remove_from_inventory(self, item):
    """Remove an item from the player's inventory."""
    if item in self.inventory:
      self.inventory.remove(item)
      return True
    return False

  def get_inventory(self):
    """Return a list of the player's inventory items."""
    return self.inventory

  def get_inventory_item(self, item_name):
    """Retrieve an item from the inventory by its name."""
    for item in self.inventory:
      if item.name.lower() == item_name.lower():
        return item
    return None