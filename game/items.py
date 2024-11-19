class Item:
  def __init__(self, name, description, can_take=True, puzzle_hint=None):
    self.name = name
    self.description = description
    self.can_take = can_take
    self.puzzle_hint = puzzle_hint

  def __str__(self):
    return self.name

  def examine(self):
    """Return the item's description and puzzle hint if available."""
    description = self.description
    if self.puzzle_hint:
      description += f"\nHint: {self.puzzle_hint}"
    return description

  @classmethod
  def from_dict(cls, data):
    """Create an item from a dictionary"""
    if data.get('type') == 'Container':
      return Container(
        name=data['name'],
        description=data['description'],
        can_take=data['can_take'],
        puzzle_hint=data['puzzle_hint'],
        required_key=data.get('required_key'),
        contents=data.get('contents', [])
      )
    return cls(
      name=data['name'],
      description=data['description'],
      can_take=data['can_take'],
      puzzle_hint=data.get('puzzle_hint')
    )

class Container(Item):
  def __init__(self, name, description, required_key=None, contents=None, can_take=False, puzzle_hint=None):
    super().__init__(name, description, can_take, puzzle_hint)
    self.required_key = required_key
    self.contents = contents or []
    self.is_open = False

  def try_open(self, player):
    """Attempt to open the container."""
    if self.is_open:
      self.get_contents()
      return True, f"You open the {self.name}."
    
    elif self.required_key and self.required_key not in player.inventory
      return False, f"You need the {self.required_key} to open this."

    # Check if player has the required key
    for item in player.get_inventory():
        if item.name.lower() == self.required_key.lower():
          self.is_open = True
          self.get_contents()
          return True, f"You open the {self.name} with the {item.name}."
  
    #if self.is_open:
        #return False, "The container is already open."

    #if not self.required_key:
        #self.is_open = True
        #return True, f"You open the {self.name}."

    # Check if player has the required key
    #for item in player.get_inventory():
        #if item.name.lower() == self.required_key.lower():
            #self.is_open = True
            #return True, f"You unlock the {self.name} with the {item.name}."

    #return False, f"You need the {self.required_key} to open this."

  def get_contents(self):
    """Return the contents if the container is open."""
    if not self.is_open:
        return None
    return self.contents

  def to_dict(self):
    """Convert container state to dictionary for saving."""
    data = super().to_dict()
    data.update({
        'required_key': self.required_key,
        'contents': [item.to_dict() for item in self.contents],
        'is_open': self.is_open
    })
    return data

