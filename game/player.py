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