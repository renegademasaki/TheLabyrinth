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